# Project_Magnet — Конфиги

## Горячая перезагрузка (без рестарта сервера)
Просто сохрани файл — сервер подхватит изменения автоматически через 300мс.

---

## brawlpass.json — Бравл Пасс

| Поле | Описание |
|------|----------|
| `season_id` | Номер сезона |
| `pass_price_gems` | Цена БП в гемах (169) |
| `pass_plus_price_gems` | Цена БП+ в гемах (249) |
| `pass_plus_bonus_tiers` | Бонусные уровни БП+ (8) |
| `end_time_days` | Дней до конца сезона (70) |
| `post_pass_xp_per_big_box` | Опыт для большого ящика после 70 уровня (500) |

### Типы наград (`type`):
- `Box` — ящик
- `BigBox` — большой ящик  
- `MegaBox` — мегаящик
- `Gems` — гемы
- `Gold` — монеты
- `PowerPoints` — очки силы
- `Skin` — скин (нужен `skin_id`)
- `Brawler` — боец (нужен `brawler_id`)
- `Pin` — значок (нужен `pin_id`)
- `PinPack` — набор значков

---

## shop.json — Магазин

Каждый оффер:
```json
{
  "title": "Название",
  "background": "default",
  "price_type": "Gems",   // или "Gold"
  "price": 80,
  "old_price": 160,        // зачёркнутая цена (скидка)
  "is_daily": true,        // ежедневный оффер
  "confirm_purchase": false,
  "items": [
    {"type": "BigBox", "amount": 3},
    {"type": "Gold", "amount": 1000}
  ]
}
```

---

## Telegram бот

Команды (только для ADMIN_ID):
- `/status` — статус сервера
- `/players` — количество онлайн
- `/reload` — принудительно перезагрузить конфиги

Переменные окружения:
```
TELEGRAM_TOKEN=токен_от_BotFather
ADMIN_ID=твой_telegram_id
```
