# airport_lookup.py

import csv
import os

csv_path = os.path.join(os.path.dirname(__file__), "static", "airports.csv")

city_to_iata = {}

def normalize(city_name):
    if not city_name:
        return ""
    return " ".join(city_name.strip().lower().split())

try:
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["type"] != "large_airport":
                continue
            city = row["municipality"]
            iata = row["iata_code"]
            if city and iata:
                city_to_iata[normalize(city)] = iata.strip()
except FileNotFoundError:
    print("CSV file not found:", csv_path)

def get_iata_code(city):
    return city_to_iata.get(normalize(city), None)
