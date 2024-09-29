from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=70b5bd0b714a64559c26ef018e7ac27f'
    city = 'salem'
    r = requests.get(url.format(city)).json()
    # print(r.text)
    temp_kelvin = r['main']['temp']
    temp_fahrenheit = round(temp_kelvin - 273.15) * 9/5 + 32
    
    city_weather = {
        'city' : city,
        'temperature'  : temp_fahrenheit,                     #r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon']
    }
    
    context = {'city_weather' : city_weather}
    # print(city_weather)
    return render(request,'weather/weather.html',context)