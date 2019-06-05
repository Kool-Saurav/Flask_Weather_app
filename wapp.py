import requests
import urllib.request
import json
from requests import get

from flask import Flask, render_template, request


app = Flask(__name__)
token = '8c8bb2bdc23b482c5b0c4ba8be73e605'


@app.route('/', methods=['GET', 'POST'] )
def weather():
    ip = get('https://ipapi.co/ip/').text
    api = 'http://api.ipstack.com/' + ip + '?access_key=' + token + '&format=1'
    result = urllib.request.urlopen(api).read()
    result = result.decode()
    result = json.loads(result)
    city = result["city"]
    if request.method == 'POST':
        new_city = request.form.get('city')
        city = new_city
    url = 'http://api.apixu.com/v1/forecast.json?key=207f6d2191a4429eb2e153427191805&q={}&days=3'
    r = requests.get(url.format(city)).json()
    weather = {
        'city': city,
        'temperature': r['current']['temp_c'],
        'condition': r['current']['condition']['text'],
        'icon': r['current']['condition']['icon'],
    }
    f_data = []
    for i in range(3):
        data_d = {
            'forecastdate': r['forecast']['forecastday'][i]['date'],
            'maxtemp': r['forecast']['forecastday'][i]['day']['maxtemp_c'],
            'mintemp': r['forecast']['forecastday'][i]['day']['mintemp_c'],
            'conditionf': r['forecast']['forecastday'][i]['day']['condition']['text'],
            'iconf': r['forecast']['forecastday'][i]['day']['condition']['icon']
        }
        f_data.append(data_d)
    return render_template('index_2.html', weather=weather, f_data = f_data)

if __name__ == '__main__':
    app.run(debug = True)


