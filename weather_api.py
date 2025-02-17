import requests

def fetch_weather_data(location):
    api_key = '2b8610e5969dca6b4b2ac79ead6eee85'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return temperature, humidity, wind_speed
    else:
        return None, None, None
