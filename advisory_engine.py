class AdvisoryEngine:
    def analyze_weather(self, weather_data, crop_name, requirements):
        """
        Compares current weather against crop requirements to generate advice.
        """
        report = []

        # 1. Check Temperature
        curr_temp = weather_data['temp']
        if curr_temp < requirements['min_temp']:
            report.append(f"[COLD ALERT] It's {curr_temp}°C. Too cold for {crop_name}. Consider using frost protection.")
        elif curr_temp > requirements['max_temp']:
            report.append(f"[HEAT ALERT] It's {curr_temp}°C. High heat stress. Increase irrigation frequency.")
        else:
            report.append(f"[TEMP OK] Temperature ({curr_temp}°C) is within the ideal range.")

        # 2. Check Humidity
        curr_humidity = weather_data['humidity']
        if curr_humidity > requirements['max_humidity']:
            report.append(f"[HUMIDITY WARNING] Humidity is {curr_humidity}%. Watch out for fungal diseases.")
        else:
            report.append(f"[HUMIDITY OK] Humidity levels are safe.")

        # 3. Rain Check
        if weather_data['rain_forecast']:
            report.append("[RAIN ALERT] Rain is expected. Do NOT spray pesticides today.")
        else:
            report.append("[CLEAR SKY] No rain forecast. Good day for fertilizer application if needed.")

        return report