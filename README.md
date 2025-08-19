# 💼 Portfolio Projects

Этот репозиторий содержит несколько учебных проектов на **Python**, созданных для портфолио и практики.  
Все проекты простые, но демонстрируют работу с API, парсинг, Telegram-ботов и автоматизацию.

---

## 📌 Содержание
- [🤖 Bot Currency](#-bot-currency)
- [🌦 Weather Parser](#-weather-parser)
- [💱 Currency Alert Bot](#-currency-alert-bot)

---

## 🤖 Bot Currency
Telegram-бот для получения актуальных курсов валют.

### 🚀 Возможности:
- Получение курса валют к рублю через **ЦБ РФ** или международные API.
- Конвертация в формате:  
100 USD in EUR
- Кнопки для популярных валют с флагами.
- Графики изменения курса (7 / 30 / 90 дней).
- Приветственная заставка и закреплённое сообщение.

### ▶ Запуск

cd bot_currency
pip install -r requirements.txt
python main.py

🌦 Weather Parser

Консольный скрипт для получения прогноза погоды.

🚀 Возможности:
	•	Парсинг прогноза через OpenWeather API.
	•	Ввод города → вывод текущей температуры, влажности, описания погоды.
	•	Минимальная и максимальная температура на день.

▶ Запуск
cd weather_parser
pip install -r requirements.txt
python weather.py

💱 Currency Alert Bot

Консольный скрипт для отслеживания курса валют.

🚀 Возможности:
	•	Проверка курса валют (USD, EUR и др.) к рублю через ЦБ РФ.
	•	Настройка порога: уведомляет, если курс выше или ниже заданного значения.
	•	Удобен для быстрого мониторинга.

▶ Запуск
cd currency_alert_bot
pip install -r requirements.txt
python bot.py

🛠 Стек технологий
	•	Python 3.10+
	•	requests
	•	python-telegram-bot
	•	matplotlib
	•	dotenv

📧 Контакты

Автор: dwtermik
Telegram: @dwtermik