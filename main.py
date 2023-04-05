import requests
import json
import pyttsx3
engine = pyttsx3.init()
city = input("Enter the name of the city \n")

url = f"https://api.weatherapi.com/v1/current.json?key=c05b293847294423b8e110331230104&q={city}&aqi=no"
r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
condition = wdic["current"]["condition"]["text"]
engine.say(f"The current weather in {city} is {w} degrees and condition is {condition}")
engine.runAndWait()