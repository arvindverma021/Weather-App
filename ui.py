import tkinter as tk
from weather_api import fetch_weather_data
from database import save_to_history
from logging_config import log_operation

def run_gui():
    def get_weather():
        location = entry.get()
        temperature, humidity, wind_speed = fetch_weather_data(location)
        if temperature is not None:
            result_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s")
            save_to_history(location, temperature, humidity, wind_speed)
            log_operation(location, temperature, humidity, wind_speed)
        else:
            result_label.config(text="Error fetching data.")

    root = tk.Tk()
    root.title("Weather Application")

    label = tk.Label(root, text="Enter location:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Get Weather", command=get_weather)
    button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()
