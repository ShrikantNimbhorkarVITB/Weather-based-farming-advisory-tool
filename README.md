# 🌾 Smart Farming Advisory Tool

## 📌 Project Overview
The **Smart Farming Advisory Tool** is a Python-based application designed to assist farmers in making informed decisions. By analyzing real-time weather conditions (Temperature, Humidity, and Rainfall) and comparing them with specific crop requirements, the system generates actionable advice to optimize yield and prevent crop damage.

## ✨ Key Features
* **Weather Analysis:** Fetches (simulated) real-time weather data for any specific location.
* **Crop Database:** Contains specific growth requirements for crops like Wheat, Rice, Cotton, Apple, and more.
* **Intelligent Advisory:** Uses a rule-based engine to warn about frost, heat stress, fungal risks, or spraying constraints.
* **Activity Logging:** Automatically logs all user sessions and advisories to `app.log` for record-keeping.
* **Interactive Menu:** Simple Command Line Interface (CLI) easy for anyone to use.

## 🛠️ Technologies Used
* **Language:** Python 3.x
* **Modules:** * `random` & `time` (Data Simulation)
    * `logging` (System Monitoring)
    * `sys` (System Control)
* **Concepts Applied:** Object-Oriented Programming (OOP), Exception Handling, Modular Architecture.

## 📂 Project Structure
```text
Farming_Tool/
│
├── main.py                 # Entry point (Run this file)
├── weather_service.py      # Handles weather data retrieval
├── crop_manager.py         # Manages crop database
├── advisory_engine.py      # Logic for generating advice
├── logger_config.py        # Logging configuration
└── README.md               # Project Documentation