import sys
import unittest
from weather_service import WeatherService
from crop_manager import CropManager
from advisory_engine import AdvisoryEngine
from logger_config import setup_logging

# ==========================================
#  INTERNAL TEST SUITE (Diagnostics Mode)
# ==========================================
class SystemDiagnostics(unittest.TestCase):
    """
    This class lives inside main.py to allow 'on-the-fly' testing
    of the system components without needing a separate file.
    """
    def setUp(self):
        print("\n   [DIAGNOSTIC] Initializing components...")
        self.crops = CropManager()
        self.advisor = AdvisoryEngine()
        self.weather = WeatherService()

    def test_1_database_integrity(self):
        print("   [CHECK] Verifying Crop Database connection...")
        # Check if we can fetch 'Wheat'
        data = self.crops.get_crop_data("Wheat")
        self.assertIsNotNone(data, "Critical: Wheat data missing from DB")
        print("   [PASS] Database is readable.")

    def test_2_advisory_logic(self):
        print("   [CHECK] Testing Logic Engine (Heat Warning)...")
        # Simulate hot weather
        hot_weather = {'temp': 35, 'humidity': 40, 'rain_forecast': False}
        wheat_data = self.crops.get_crop_data("Wheat")
        
        # Generate advice
        advice = self.advisor.analyze_weather(hot_weather, "Wheat", wheat_data)
        full_text = " ".join(advice)
        
        # Expecting a heat alert
        self.assertIn("HEAT ALERT", full_text, "Logic Error: Failed to detect high temp.")
        print("   [PASS] Logic Engine correctly flagged heat stress.")

    def test_3_weather_connection(self):
        print("   [CHECK] Testing Weather Service API simulation...")
        data = self.weather.get_weather("Test City")
        self.assertIn('temp', data)
        print("   [PASS] Weather service returned valid data structure.")

# ==========================================
#  MAIN APPLICATION LOGIC
# ==========================================
class FarmingTool:
    def __init__(self):
        # Initialize all our helper classes
        self.logger = setup_logging()
        self.weather = WeatherService()
        self.crops = CropManager()
        self.advisor = AdvisoryEngine()

    def display_menu(self):
        print("\n" + "="*42)
        print("   🌾 FARMER'S ASSISTANT TOOL v2.0 🌾")
        print("="*42)
        print("1. Check Weather & Get Advice")
        print("2. View Supported Crops")
        print("3. Run System Diagnostics (Self-Test)")  # New Option
        print("4. Exit")
        print("="*42)

    def run_diagnostics(self):
        print("\n" + "!"*40)
        print("   ENTERING DIAGNOSTIC MODE...")
        print("!"*40)
        # This magic code runs the tests without killing the main app
        suite = unittest.TestLoader().loadTestsFromTestCase(SystemDiagnostics)
        unittest.TextTestRunner(verbosity=0).run(suite)
        print("\n[INFO] Diagnostics complete. Returning to menu...")

    def run(self):
        self.logger.info("Application started by user.")
        
        while True:
            self.display_menu()
            choice = input("Select an option (1-4): ").strip()

            if choice == '1':
                # --- FEATURE 1: Main Advisory ---
                user_crop = input("\nEnter your crop name: ").strip()
                crop_data = self.crops.get_crop_data(user_crop)

                if not crop_data:
                    print(f"❌ Sorry, we don't have data for '{user_crop}' yet.")
                    print("Try checking the supported crops list.")
                    continue

                location = input("Enter your city/village name: ").strip()
                if not location: location = "Unknown Location"

                current_weather = self.weather.get_weather(location)
                
                if current_weather:
                    print(f"\n--- 🌤 WEATHER REPORT FOR {location.upper()} ---")
                    print(f"Temp: {current_weather['temp']}°C | Humidity: {current_weather['humidity']}%")
                    
                    print(f"\n--- 🚜 ADVICE FOR {user_crop.upper()} ---")
                    advice_list = self.advisor.analyze_weather(current_weather, user_crop, crop_data)
                    for tip in advice_list:
                        print(f"-> {tip}")
                    
                    self.logger.info(f"Advice generated for {user_crop} at {location}")
                else:
                    print("Error: Could not fetch weather. Please try again.")

            elif choice == '2':
                # --- FEATURE 2: List Crops ---
                print("\nWe currently support these crops:")
                print(", ".join(self.crops.get_all_crop_names()))

            elif choice == '3':
                # --- FEATURE 3: Internal Tests ---
                self.run_diagnostics()

            elif choice == '4':
                print("\nExiting... Have a productive harvest!")
                break

            else:
                print("\nInvalid choice. Please type 1, 2, 3, or 4.")

if __name__ == "__main__":
    app = FarmingTool()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
        sys.exit()