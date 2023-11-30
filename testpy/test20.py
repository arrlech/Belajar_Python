from flask import Flask, jsonify
import cv2
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
OPENWEATHERMAP_API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'

@app.route('/api/get_temperature', methods=['GET'])
def get_user_location():
    ipinfo_url = 'http://ipinfo.io/json'
    response = requests.get(ipinfo_url)
    data = response.json()
    location = data.get('loc', '').split(',')
    if len(location) == 2:
        return float(location[0]), float(location[1])
    return None

def get_weather(latitude, longitude):
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={OPENWEATHERMAP_API_KEY}'
    response = requests.get(url)
    data = response.json()
    temperature_kelvin = data['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15
    return temperature_celsius

@app.route('/api/get_temperature', methods=['GET'])
def get_temperature():
    user_location = get_user_location()

    if user_location:
        latitude, longitude = user_location
        temperature_camera = 25.0  # Placeholder for camera temperature
        temperature_weather = get_weather(latitude, longitude)

        response = {
            'temperature_camera': round(temperature_camera, 2),
            'temperature_weather': round(temperature_weather, 2)
        }
    else:
        response = {'error': 'Unable to get user location'}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
