# Currency Alert Bot
Телеграм-бот для уведомлений о курсах валют.

## Установка
1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Создайте `.env`:
   ```
   TG_TOKEN=ваш_токен
   TG_CHAT_ID=ваш_chat_id
   ```

## Настройка
В `settings.json` укажите пороговые значения:
```json
{
    "USD": {"min": 85, "max": 100},
    "EUR": {"min": 90, "max": 110}
}
```

## Запуск
```bash
python alert_bot.py
```