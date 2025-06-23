import requests
import json
def weather(city):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=966ef49f4dd5066506988f5892b4bfc9&units=metric"
    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()
        
        temperature=data["main"]["temp"]
        humidity=data["main"]["humidity"]
        feels_like=data["main"]["feels_like"]
        pressure=data["main"]["pressure"]
        ground_level=data["main"]["grnd_level"]
        visibility=data["visibility"]
        wind_speed=data["wind"]["speed"]
        timezone=data["timezone"]
        
        
        print(f"Weather in {city}:")
        print(f"Temperature:{temperature}°C(Feels like:{feels_like}°C)")
        print(f"Humidity:{humidity}%")
        print(f"Description:{data["weather"][0]["description"].capitalize()}")
        print(f"Pressure:{pressure}")
        print(f"Ground level:{ground_level}")
        print(f"Visibilty:{visibility}")
        print(f"Wind_speed:{wind_speed}")
        print(f"Timezone:{timezone}")
        
    except requests.exceptions.RequestException as e:
        print("error fetching error data: {e}")
city=input("Enter city name:")
weather(city)