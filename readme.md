# Weather Application

This is a Python-based weather application that fetches real-time weather data for a city or location from a public API (OpenWeatherMap or WeatherStack).

## Features
- Fetch weather data: temperature, humidity, wind speed.
- Search history stored in SQLite.
- Optional Tkinter-based GUI for a better user experience.
  
## Requirements
- Python 3.x
- `requests` library: Install using `pip install requests`
- `sqlite3` (standard with Python)
- `tkinter` (standard with Python)

## Setup
1. Install necessary packages:
    ```
    pip install requests
    ```
2. Obtain an API key from OpenWeatherMap or WeatherStack and add it to `config.py`.
3. Run the application:
    - Console app: `python app.py`
    - Tkinter app (optional): `python gui.py`

## Functionality
- Search for weather data by city name.
- View past search history.
