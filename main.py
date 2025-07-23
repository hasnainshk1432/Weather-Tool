import requests

API_KEY = "b1385c23bcac0fafa6d404131748df89"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    print(data)  # 👈 TEMPORARY for debugging

    if response.status_code == 200:
        weather = data['weather'][0]['description'].title()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        print(f"\n📍 Weather in {city.capitalize()}:")
        print(f"🌤 Condition : {weather}")
        print(f"🌡 Temperature : {temp}°C")
        print(f"💧 Humidity : {humidity}%")
    else:
        print("\n❌ Error:", data.get("message", "Failed to fetch weather data."))

def main():
    print("=== 🌦 Welcome to Weather App ===")
    city = input("Enter a city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
