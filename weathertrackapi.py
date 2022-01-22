# from urllib import response
# from wsgiref.util import request_uri
import requests

API_KEY = "PASTE IT HERE"
BASE_URL = "URL OF OPEN WEATHER MAP"

city =input("Enter a city name: ")
request_url = f"{BASE_URL}?appid{API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code ==200:
    data =response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"]-273.15, 2)

    print("Weather: ", weather)
    print("Temperature: ", temperature, "celsius")
else:
    print("An error occured")

