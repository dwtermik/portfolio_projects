import requests
import time
import json
import os

TOKEN = os.getenv("TG_TOKEN")  # Токен бота
CHAT_ID = os.getenv("TG_CHAT_ID")  # ID чата
CBR_URL = "https://www.cbr-xml-daily.ru/daily_json.js"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

def check_currency():
    with open("settings.json", "r") as f:
        settings = json.load(f)

    res = requests.get(CBR_URL).json()
    valutes = res["Valute"]

    for code, cfg in settings.items():
        if code not in valutes:
            continue
        rate = valutes[code]["Value"]
        if rate >= cfg["max"] or rate <= cfg["min"]:
            send_message(f"⚠ {code} = {rate}₽ (порог {cfg['min']}–{cfg['max']})")

if __name__ == "__main__":
    print("Бот уведомлений запущен...")
    while True:
        check_currency()
        time.sleep(3600)  # раз в час
