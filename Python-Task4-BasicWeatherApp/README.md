# Advanced Weather App (Task 4)

A desktop-based weather forecaster application built with Python's `tkinter` GUI framework. It integrates with the OpenWeatherMap API and IP geolocation services to fetch and display real-time weather information, hourly breakdowns, and a 5-day forecast.

---

## Tech Stack
- **Language**: Python 3.x
- **GUI Framework**: `tkinter`
- **APIs & Web**: `requests`, OpenWeatherMap API, IPInfo API
- **Image Processing**: `Pillow` (PIL) for weather icon rendering
- **Utilities**: `io`, `datetime`

---

## Key Features
- **Real-Time Weather Fetching**: Retrieves current temperature, high/low records, humidity, wind speed, and weather descriptions for any city or ZIP code.
- **Auto-Detect Location**: Automatically detects the user's current city based on IP geolocation (`ipinfo.io`) via a dedicated button.
- **Hourly & 5-Day Forecasts**: Displays multi-interval hourly breakdowns and structured 5-day daily forecasts.
- **Unit Conversion**: Toggle seamlessly between Celsius (°C) and Fahrenheit (°F) at runtime.
- **Visual Weather Icons**: Dynamically downloads and displays official OpenWeatherMap condition icons using Pillow.
- **Error Handling & Feedback**: Robust management of network timeouts, invalid inputs, and API authentication failures.

---

## Setup & Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/LavanyaTrivedi25/OIRSIP.git
   cd Python-Task4-BasicWeatherApp
