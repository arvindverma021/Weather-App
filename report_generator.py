import pandas as pd
import sqlite3

def generate_report():
    connection = sqlite3.connect('weather_history.db')
    df = pd.read_sql_query("SELECT * FROM weather_history", connection)
    connection.close()

    df.to_csv('weather_report.csv', index=False)
    print("Report generated: weather_report.csv")
