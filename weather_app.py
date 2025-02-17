from ui import run_gui
from weather_api import fetch_weather_data
from database import save_to_history
from report_generator import generate_report
from logging_config import log_operation

def console_interface():
    location = input("Enter the city or coordinates (latitude,longitude): ")
    temperature, humidity, wind_speed = fetch_weather_data(location)

    if temperature is not None:
        print(f"Weather in {location}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        save_to_history(location, temperature, humidity, wind_speed)
        log_operation(location, temperature, humidity, wind_speed)
    else:
        print("Couldn't fetch weather data.")

def main():
    choice = input("Do you want to use Console or Tkinter (GUI)? (console/tkinter): ").strip().lower()
    if choice == "console":
        console_interface()
    elif choice == "tkinter":
        run_gui()
    else:
        print("Invalid choice. Please choose 'console' or 'tkinter'.")
        main()

if __name__ == "__main__":
    main()
