import requests
from geopy.geocoders import Nominatim
import json

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

API_KEY = 'U9gnPUgPAUkpSnxLfXzbVQUFwpFFgE77'
API_URL = 'https://api.windy.com/api/point-forecast/v2'

location = geolocator.geocode(input('Enter Location:'))

payload = {
    "key": API_KEY,
    "model": "namConus",
    "lat": location.latitude,
    "lon": location.longitude,
    "parameters": ["temp", "precip", "ptype", "pressure"]
}

response = requests.post(API_URL, json= payload)

# 200: Success
if response.status_code == 200:
    data = response.json()
    print(data)
# 204: No matching parameters
elif response.status_code == 204:
    print('No matching results found.')

# 400: Invalid request
elif response.status_code == 400:
    print(response.text)

# 500: Unexpected Error
# elif response.status_code == 500:
# Catchall
else:
    print('Error fetching weather data')