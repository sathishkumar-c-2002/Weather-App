from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=70b5bd0b714a64559c26ef018e7ac27f'
    city = 'salem'
    r = requests.get(url.format(city)).json()
    # print(r.text)
    city_weather = {
        'city' : city,
        'temperature'  : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon']
    }
    print(city_weather)
    return render(request,'weather/weather.html')