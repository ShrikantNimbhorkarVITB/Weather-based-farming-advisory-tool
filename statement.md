<!-- Created by Shrikant Nimbhorkar for VITyarthi Project Assessment. -->

# Project Problem Statement & Scope

## 1. Problem Statement
Agriculture is highly dependent on weather conditions. However, many small-scale farmers lack access to timely, specific advice that correlates weather forecasts with their specific crop needs. This leads to:
* Crop damage due to unexpected frost or heat.
* Wastage of fertilizers/pesticides due to rain washing them away.
* Disease outbreaks caused by ignored humidity levels.

There is a need for a simple, digital solution that acts as a bridge between raw weather data and actionable farming decisions.

## 2. Target Users
* **Small to Medium Farmers:** Who need quick decision support.
* **Agricultural Students:** For learning about crop-weather relations.
* **Local Extension Workers:** To assist farmers in rural areas.

## 3. Project Scope
The current version of the **Smart Farming Advisory Tool** covers:
* **Input:** User selects a crop and provides a location.
* **Processing:** The system simulates weather retrieval and compares it against a pre-defined database of crop constraints (Min/Max Temp, Max Humidity).
* **Output:** A text-based report offering warnings (Cold/Heat Alerts) and suggestions (Spraying conditions).

## 4. High-Level Features
1.  **Crop Requirement Management:** Ability to store and retrieve temperature/humidity thresholds for varying crops.
2.  **Weather Simulation Engine:** Mimics real-world weather variability for testing purposes.
3.  **Advisory Logic:** Conditional algorithms that trigger specific warnings based on data comparison.
4.  **Robust Error Handling:** Ensures the system doesn't crash if data is missing or inputs are invalid.