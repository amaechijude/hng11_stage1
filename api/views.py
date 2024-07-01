from django.shortcuts import render, redirect
from django.http.response import JsonResponse

import requests
from decouple import config


api_key = config('WEATHER_API')
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


ip_address = get_ip()
response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

def get_location(request):
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return JsonResponse(location_data, safe=False)

api_key = config('WEATHER_API')
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = response.get("city")