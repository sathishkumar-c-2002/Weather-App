from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=70b5bd0b714a64559c26ef018e7ac27f'
    city = 'salem'
     
     
    if request.method == 'POST':
        # print(request.POST)
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()
    
    cities = City.objects.all()
    
    weather_data = []
    
    for city in cities:
        
        r = requests.get(url.format(city)).json()
        # print(r.text)
        
        temp_kelvin = r['main']['temp']
        temp_fahrenheit = round(temp_kelvin - 273.15) * 9/5 + 32
        
        city_weather = {
            'city' : city.name,
            'temperature'  : temp_fahrenheit,                     #r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon']
        }
        
        weather_data.append(city_weather)
    print(weather_data)
    context = {'weather_data' : weather_data,'form': form}
    # print(city_weather)
    return render(request,'weather/weather.html',context)