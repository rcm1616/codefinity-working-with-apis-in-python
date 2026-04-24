import requests

def print_first_five_paris_temperatures():
    # Your implementation goes here
    url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        "latitude": 48.85,
        "longitude": 2.35,
        "hourly": "temperature_2m"
    }
    response= requests.get(url, params=params)
    data = response.json()
    ##print(data)
    for temp in data['hourly']['temperature_2m'][:5]:
       print(temp)

print_first_five_paris_temperatures()
