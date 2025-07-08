# airport_lookup.py

city_to_iata = {
    "Cork": "ORK",
    "Dublin": "DUB",
    "London": "LON",
    # Add more cities as needed
}

def get_iata_code(city):
    return city_to_iata.get(city, None)
