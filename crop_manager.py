class CropManager:
    def __init__(self):
        # Database of crops with their ideal growing conditions.
        # Temp is min-max range (Celsius). Humidity is max limit (%).
        self.crop_database = {
            "Wheat": {"min_temp": 10, "max_temp": 25, "max_humidity": 60},
            "Rice": {"min_temp": 20, "max_temp": 35, "max_humidity": 85},
            "Tomato": {"min_temp": 18, "max_temp": 30, "max_humidity": 70},
            "Corn": {"min_temp": 18, "max_temp": 27, "max_humidity": 65},
            "Potato": {"min_temp": 15, "max_temp": 25, "max_humidity": 85},
            "Cotton": {"min_temp": 21, "max_temp": 30, "max_humidity": 50},
            "Sugarcane": {"min_temp": 20, "max_temp": 35, "max_humidity": 85},
            "Apple": {"min_temp": 15, "max_temp": 25, "max_humidity": 80}
        }

    def get_crop_data(self, crop_name):
        # Normalize input to title case to match keys (e.g. "wheat" -> "Wheat")
        formatted_name = crop_name.capitalize()
        
        if formatted_name in self.crop_database:
            return self.crop_database[formatted_name]
        else:
            return None

    def get_all_crop_names(self):
        # Helper function to display list to user
        return list(self.crop_database.keys())