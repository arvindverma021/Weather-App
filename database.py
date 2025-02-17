import sqlite3
from datetime import datetime

def create_database():
    connection = sqlite3.connect('weather_history.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_history (
                        id INTEGER PRIMARY KEY,
                        location TEXT,
                        temperature REAL,
                        humidity REAL,
                        wind_speed REAL,
                        timestamp TEXT)''')
    connection.commit()
    connection.close()

def save_to_history(location, temperature, humidity, wind_speed):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    connection = sqlite3.connect('weather_history.db')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO weather_history (location, temperature, humidity, wind_speed, timestamp)
                      VALUES (?, ?, ?, ?, ?)''', (location, temperature, humidity, wind_speed, timestamp))
    connection.commit()
    connection.close()

create_database()
