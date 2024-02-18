import requests
from config import weather_api

def get_weather(city, api_key):
    url = f'{weather_api}{city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'max_temperature': data['main']['temp_max'],
            'min_temperature': data['main']['temp_min'],
            'visibility': data.get('visibility', 'N/A')
        }
        return weather_info
    else:
        return None

def main():
    api_key = '15c58d0eceb116b830eb5274b2f5cd0d'  # Replace 'YOUR_API_KEY_HERE' with your actual API key
    city = input("Enter city name: ")
    weather = get_weather(city, api_key)

    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
        print(f"Maximum Temperature: {weather['max_temperature']}°C")
        print(f"Minimum Temperature: {weather['min_temperature']}°C")
        print(f"Visibility: {weather['visibility']} meters")
    else:
        print("City not found or invalid API key.")

if __name__ == "__main__":
    main()
