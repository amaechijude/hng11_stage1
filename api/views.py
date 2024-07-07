from django.shortcuts import render, redirect
from django.http.response import JsonResponse

from ipware import get_client_ip
import requests, time, json
from decouple import config


def index(request):
    time.sleep(1)
    return redirect('hello')


def hello(request):
    #response = requests.get('https://api64.ipify.org?format=json').json()
    visitor_name = request.GET.get('visitor_name').strip('"')
    
    #ip_address = response["ip"]

    client_ip, is_routable = get_client_ip(request)
    
    time.sleep(1)
    location = requests.get(f'https://ipapi.co/{client_ip}/json/').json()
    city = location.get("city")

    api_key = config('api_key')
    time.sleep(1)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}"
    time.sleep(1)
    resp = requests.get(url).json()
    temperature = resp.get('main', {}).get('temp')
    temperature_celsius = round(temperature - 273.15, 2)
    greeting = f'Hello {visitor_name}, the temperature is {temperature_celsius} degrees celcius in {city}'

    output = {
                "client_ip": client_ip,
                "location": city,
                "greeting": greeting,
            }

    #print(ip_address)
    
    return JsonResponse(output, safe=False)
    
    #except:
     #   error = {
      #          "error": "Connection Error",
       #         }
        #return JsonResponse(error, safe=False)


