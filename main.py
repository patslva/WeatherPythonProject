import requests

API_KEY = "af5a088adeed2a1174bda8c7b9436138"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter the name of the city: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
# q = query appid = API key
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"]-273.15)
    print("Weather:", weather)
    print("Temperature:", temperature, "°C")

else:
    print("An error has occured")






