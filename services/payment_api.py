# services/payment_api.py
import uuid

class PaymentConnector:
    """Finansal sistemlerle konuşan, token tabanlı ödeme elçisi."""

    def generate_virtual_card(self, amount, currency="TRY"):
        # Burası gerçekte banka API'sine gidip sanal kart üretecek
        token = f"VIRTUAL-{uuid.uuid4().hex[:16].upper()}"
        print(f"💳 [PAYMENT API]: {amount} {currency} limitli sanal kart oluşturuldu.")
        return token

    def process_transaction(self, token, amount):
        # İşlem onaylandığında sistemi tetikleyen kısım
        print(f"🔒 [PAYMENT API]: {token} ile {amount} tutarında işlem onaylandı.")
        return True
