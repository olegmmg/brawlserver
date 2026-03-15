# Project_Magnet Server (BSL V41 C#)

## Запуск локально
```
dotnet run --project BSL.v41.General
```

## Telegram бот
Установи переменные окружения перед запуском:
```
set TELEGRAM_TOKEN=ВАШ_ТОКЕН_ОТ_BOTFATHER
set ADMIN_ID=ВАШ_TELEGRAM_ID
dotnet run --project BSL.v41.General
```

## Railway деплой
1. Залей на GitHub
2. Railway → New Project → GitHub repo
3. В Settings → Variables добавь:
   - TELEGRAM_TOKEN = токен от BotFather
   - ADMIN_ID = твой Telegram ID (5915637863)
4. Settings → Networking → TCP Proxy → порт 9339

## Raspberry Pi
```
sudo apt install dotnet-sdk-8.0
cd PM_BSL41
TELEGRAM_TOKEN=токен ADMIN_ID=айди dotnet run --project BSL.v41.General
```
