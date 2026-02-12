import requests

# ===== CONFIGURAÇÃO =====
TELEGRAM_TOKEN = "COLOQUE_SEU_TOKEN_AQUI"
CHAT_ID = "COLOQUE_SEU_CHAT_ID_AQUI"

CONSULADOS = [
    "https://prenotami.esteri.it/Services/Booking/123",  # Curitiba (placeholder)
    "https://prenotami.esteri.it/Services/Booking/456"   # Florianópolis (placeholder)
]

# =========================

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def check_availability():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for url in CONSULADOS:
        response = requests.get(url, headers=headers)

        if "Não há disponibilidade" not in response.text:
            send_telegram(f"🚨 POSSÍVEL VAGA ENCONTRADA!\n{url}")

if __name__ == "__main__":
    check_availability()
