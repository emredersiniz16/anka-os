# services/flight_api.py

class FlightConnector:
    """Uçak firmalarıyla konuşan elçi ajan."""
    
    def search(self, destination, time):
        print(f"📡 [CONNECTING]: {destination} uçuşları taranıyor...")
        # Burası ileride gerçek API isteği olacak (requests.get...)
        return {
            "flight_number": "TK-1923",
            "price": "4500 TL",
            "status": "Available",
            "time": time
        }

    def book(self, flight_id):
        print(f"🎫 [BOOKING]: {flight_id} için rezervasyon paketi hazırlanıyor...")
        return "PNR: XYZ-789"
