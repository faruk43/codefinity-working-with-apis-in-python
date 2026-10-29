import requests

def print_first_five_paris_temperatures():
    # Your implementation goes here
    URL = "https://api.open-meteo.com/v1/forecast" 
    params = {"latitude": 48.85, "longitude": 2.35, "hourly": "temperature_2m"}
    response = requests.get(URL, params=params)
    data = response.json()
    temperatures = data["hourly"]["temperature_2m"]

    for temp in temperatures [:5]:
        print(temp)
    
    pass

print_first_five_paris_temperatures()
