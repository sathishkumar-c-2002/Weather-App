from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=70b5bd0b714a64559c26ef018e7ac27f'
    city = 'Las Vegas'
    r = requests.get(url.format(city))
    print(r.text)
    return render(request,'weather/weather.html')