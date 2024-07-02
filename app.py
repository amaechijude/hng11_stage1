import requests, random, json
from flask import Flask,request,jsonify, redirect, url_for
from decouple import config
from urllib import request as ub

app = Flask(__name__)

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

@app.route("/")
def index():
    #visitor_name = request.args.get('visitor_name', default='Mark')
    return redirect(url_for('help'))


@app.route(r"/api/hello", methods=['GET'])
def help():
    visitor_name = request.args.get('visitor_name', default='Mark')

    WEATHER_API = config('WEATHER_API')
    ip_address = requests.get('https://api.ipify.org').text
    host_data = json.loads(requests.get(f"http://ip-api.com/json/{ip_address}").text)
    #response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    city = host_data['city']  #response.get("city")
    temprature = json.loads(ub.urlopen(f'https://api.openweathermap.org/data/2.5/weather?={city}&appid={WEATHER_API}').read())['main']['temp']
    temprature = format(temprature - 273, '.2f')
    response = {
            "name": visitor_name,
            "client_ip": ip_address,
            "greeting": f"Hello {visitor_name}!, the tempreture is {temprature} degrees Celsuils in {city} "
            }
    return jsonify(response)




if __name__ == '__main__':
    app.run(debug=True)



