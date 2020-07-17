from django.shortcuts import render
import requests
# Create your views here.
def viewapi(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR', "") or request.META.get ('REMOTE_ADDR')
    url='http://api.ipstack.com/{}?access_key=8dbebad3837fdf1ed2692b58b8fae9e3'.format(ip)
    #print(url)
    #url='http://api.ipstack.com/183.87.50.254?access_key=8dbebad3837fdf1ed2692b58b8fae9e3'
    response=requests.get(url)
    data1=response.json()
    ip=data1['ip']
    city=data1['city']
    country=data1['country_name']
    state=data1['region_name']
    zip=data1['zip']
    url1= "http://api.weatherstack.com/current?access_key=60768302a7b56a70daa391f5ef171152&query={}".format(city)
    #print(url1)
    response=requests.get(url1)
    data=response.json()
    temp=data["current"]["temperature"]
    wetherdescription=(data["current"]["weather_descriptions"][0])
    windspeed=data["current"]["wind_speed"]
    winddegree=data["current"]["wind_degree"]
    pressure=data["current"]["pressure"]
    humidity=data["current"]["humidity"]
    dict={
        'ip':ip,
        'city':city,
        'country':country,
        'state':state,
        'zip':zip,
        'temp':temp,
        'wetherdescription':wetherdescription,
        'windspeed':windspeed,
        'winddegree':winddegree,
        'pressure':pressure,
        'humidity':humidity,
        }

    return render(request,'testapp/display.html',dict)