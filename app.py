#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    api_key = 'YOUR_API_KEY'
    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=2&aqi=no&alerts=no'
    response = requests.get(url)
    weather_data = response.json()
    
    if 'error' not in weather_data:
        weather = {
            'city': weather_data['location']['name'],
            'country': weather_data['location']['country'],
            'temperature': weather_data['current']['temp_c'],
            'condition': weather_data['current']['condition']['text'],
            'icon': weather_data['current']['condition']['icon'],
            'forecast': weather_data['forecast']['forecastday']
        }
        return render_template('result.html', weather=weather)
    else:
        return render_template('index.html', error='City not found')

if __name__ == '__main__':
    app.run(debug=True)
