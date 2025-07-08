import requests

def search_flights(city_from, travel_date):
    url = "https://api.skypicker.com/flights"
    params = {
        "fly_from": city_from,
        "date_from": travel_date,
        "date_to": travel_date,
        "partner": "picky",  # this works without auth
        "curr": "EUR",
        "limit": 5,
        "sort": "price"
    }

    response = requests.get(url, params=params)
    return response.json()