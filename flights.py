# flights.py
import requests

API_KEY = "fc4a1e43bd1163b0ef1a0ce7c2b8000f"

def search_flights(iata_code, travel_date):
    url = "http://api.aviationstack.com/v1/flights"
    params = {
        "access_key": API_KEY,
        "dep_iata": iata_code,
        "flight_date": travel_date,
        "limit": 10
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Error fetching data from Aviationstack:", e)
        return []

    data = response.json()

    # ✅ THIS is the correct loop:
    flights = []
    for item in data.get("data", []):
        flights.append({
            "airline": item.get("airline", {}).get("name", "Unknown Airline"),
            "flight_number": item.get("flight", {}).get("iata", "Unknown"),
            "destination": item.get("arrival", {}).get("iata", "Unknown"),
            "departure_time": item.get("departure", {}).get("scheduled", "Unknown"),
            "status": item.get("flight_status", "Unknown")
        })

    # Add this to see what's coming back!
    print("Aviationstack response:", data)

    return flights
