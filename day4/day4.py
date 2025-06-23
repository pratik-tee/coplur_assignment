
'''import csv
data=[
    ["name","age","country"],
    ["ram",23,"usa"],
    ["shyam",21,"india"],
    ["gahan",34,"ukrain"]
]

with open("data.csv","w",newline="") as file:   #For writing the data in csv file
    writer = csv.writer(file)
    for x in data:
        writer.writerow(x)
        
        
with open("data.csv","r") as file:          #For reading the data in csv  file 
    reader=csv.reader(file)
    for x in reader:
        print(x)
        

#Exception handling
try:
    n=int(input("Enter number"))
    m=20/n
    print(m)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Number is required")
    
#API
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
        
        print(f"Weather in {city}:")
        print(f"Temperature:{temperature}°C(Feels like:{feels_like}°C)")
        print(f"Humidity:{humidity}%")
        print(f"Description:{data["weather"][0]["description"].capitalize()}")
        
    except requests.exceptions.RequestException as e:
        print("error fetching error data: {e}")
city=input("Enter city name:")
weather(city)
'''
#sqlite
import sqlite3
conn=sqlite3.connect("db1.db")

conn.execute('''
             Create table users2(
                 usid INTEGER PRIMARY KEY AUTOINCREMENT,
                 usnm VARCHAR(100),
                 pass VARCHAR(100),
                 email VARCHAR(50)
             )
             ''')
conn.close()