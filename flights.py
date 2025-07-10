import requests

API_KEY = "fc4a1e43bd1163b0ef1a0ce7c2b8000f"

def search_flights(iata_code):
    url = "http://api.aviationstack.com/v1/flights"
    params = {
        "access_key": API_KEY,
        "dep_iata": iata_code,
        "limit": 10
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Error fetching data from Aviationstack:", e)
        return []

    data = response.json()

    flights = []
    for item in data.get("data", []):
        flight_num = item.get("flight", {}).get("iata", "")
        tracking_url = None
        if flight_num:
            tracking_url = f"https://www.flightradar24.com/data/flights/{flight_num.lower()}"

        flights.append({
            "airline": item.get("airline", {}).get("name", "Unknown Airline"),
            "flight_number": flight_num or "Unknown",
            "destination": item.get("arrival", {}).get("iata", "Unknown"),
            "departure_time": item.get("departure", {}).get("scheduled", "Unknown"),
            "status": item.get("flight_status", "Unknown"),
            "tracking_url": tracking_url
        })

    return flights
