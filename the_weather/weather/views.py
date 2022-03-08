from django.shortcuts import render
import requests
from .forms import CityForm
from .models import WeatherData
from django.contrib import messages

def index(request):

    url ='http://api.openweathermap.org/data/2.5/weather?q={}&appid=f621c10d37d86f7b8d4f43ff3aca7a66'
    msg = "Check the weather of your city"
    msg_class = ""
    error_msg = ""
    if request.method=='POST':

        city=request.POST['city']
        city_weather = requests.get(
            url.format(city)).json()  # request the API data and convert the JSON to Python data types
        print(city_weather)

        if city_weather['cod']==200:
            temperature=city_weather['main']['temp'],
            description=city_weather['weather'][0]['description'],
            icon=city_weather['weather'][0]['icon']

            data=WeatherData(name=city,temp=float(temperature[0]),description=description[0],icon=icon)
            data.save()
            msg="City Weather data Successfully"
        else:
            error_msg="City is not found"

        if error_msg:
            msg=error_msg
            msg_class="is-danger"

        else:
            msg_class="is-success"
    weather_data=WeatherData.objects.all()
    context = {'weather_data': weather_data,'msg':msg,'msg_class':msg_class}

    return render(request, 'weather/index.html', context)





def filter_data(request):
    context={}
    if request.method=='POST':
        city=request.POST['city']
        date_from=request.POST['d1']
        date_to=request.POST['d2']

        data=WeatherData.objects.filter(name=city)
        date_range=WeatherData.objects.raw('Select id,name,temp,description,icon,date from weather_data where date between"'+date_from+'"and"'+date_to+'"')
        context={'range':date_range}
        print(context)
    return render(request, 'weather/filter_data.html', context)