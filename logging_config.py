import logging

def setup_logging():
    logging.basicConfig(filename='weather_operations.log', level=logging.INFO,
                        format='%(asctime)s - %(message)s')

def log_operation(location, temperature, humidity, wind_speed):
    logging.info(f"{location} - Temp: {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s")
