import unittest
from crop_manager import CropManager
from advisory_engine import AdvisoryEngine
from weather_service import WeatherService

class TestFarmingTool(unittest.TestCase):

    def setUp(self):
        """
        This runs before every single test.
        It's like starting a fresh session for each check.
        """
        print("\n[SETUP] Initializing modules for testing...")
        self.crops = CropManager()
        self.advisor = AdvisoryEngine()
        self.weather = WeatherService()

    def tearDown(self):
        """
        Runs after every test. just to make the output look clean.
        """
        print("[TEARDOWN] Test complete.\n")

    def test_1_crop_data_found(self):
        # Test if we can actually find a crop that exists
        print("--> Testing: Can we find 'Wheat' in the database?")
        
        crop_name = "Wheat"
        result = self.crops.get_crop_data(crop_name)
        
        # We expect a dictionary, not None
        self.assertIsNotNone(result, "Error: Wheat should exist but returned None")
        
        # Check specific values to be sure
        print(f"    Found data: {result}")
        self.assertEqual(result['min_temp'], 10, "Min temp for Wheat should be 10")

    def test_2_crop_data_missing(self):
        # Test what happens if the user types a nonsense crop
        print("--> Testing: What happens if we search for 'Moon Rice'?")
        
        crop_name = "Moon Rice"
        result = self.crops.get_crop_data(crop_name)
        
        # This time, we EXPECT it to be None
        self.assertIsNone(result, "Error: System should return None for invalid crops")
        print("    System correctly returned None.")

    def test_3_heat_warning_logic(self):
        # Let's simulate a really hot day and see if the system warns us
        print("--> Testing: Heat Wave Logic")
        
        # 35 degrees is definitely too hot for Wheat (limit is 25)
        hot_weather_mock = {
            'temp': 35, 
            'humidity': 40, 
            'rain_forecast': False
        }
        
        # Get the requirements for Wheat
        wheat_reqs = self.crops.get_crop_data("Wheat")
        
        # Generate the advice
        advice_output = self.advisor.analyze_weather(hot_weather_mock, "Wheat", wheat_reqs)
        
        # Check if the words "HEAT ALERT" appear in any of the advice strings
        found_alert = False
        for tip in advice_output:
            if "HEAT ALERT" in tip:
                found_alert = True
                print(f"    Success! Found warning: '{tip}'")
        
        self.assertTrue(found_alert, "Failed: System did not warn about high temperature!")

    def test_4_rain_warning_logic(self):
        # Testing if the system catches rain
        print("--> Testing: Rain Forecast Logic")
        
        rainy_weather_mock = {
            'temp': 20, 
            'humidity': 60, 
            'rain_forecast': True  # It is raining
        }
        
        wheat_reqs = self.crops.get_crop_data("Wheat")
        advice_output = self.advisor.analyze_weather(rainy_weather_mock, "Wheat", wheat_reqs)
        
        # We need to make sure it tells us NOT to spray pesticides
        advice_text = " ".join(advice_output)
        
        self.assertIn("RAIN ALERT", advice_text, "Failed: System missed the rain warning.")
        print("    System correctly warned about rain.")

    def test_5_weather_structure(self):
        # Just checking if the weather service returns the keys we expect
        print("--> Testing: Weather Data Keys")
        
        data = self.weather.get_weather("Test Location")
        
        # It should have temp, humidity, and rain_forecast
        self.assertIn('temp', data)
        self.assertIn('humidity', data)
        self.assertIn('rain_forecast', data)
        print("    Weather data format looks correct.")

if __name__ == '__main__':
    # This block actually runs the tests when you type 'python test.py'
    print("==========================================")
    print("   STARTING SYSTEM DIAGNOSTICS")
    print("==========================================")
    unittest.main()