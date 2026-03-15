import telebot
import json
import sqlite3
import os
from Database.DBManager import DB

# Настройки
TOKEN = "7409885326:AAHiR57aiYIy28GQzJGMTNjial1CRB7DGiM"
ADMIN_IDS = [8400748805]  # Ваш ID в Telegram

bot = telebot.TeleBot(TOKEN)
db = DB()

# Команда /gems
@bot.message_handler(commands=['gems'])
def give_gems(message):
    try:
        # Проверяем права администратора
        if message.from_user.id not in ADMIN_IDS:
            bot.reply_to(message, "❌ У вас нет прав для этой команды!")
            return
        
        # Парсим команду: /gems [ID] [количество]
        parts = message.text.split()
        if len(parts) != 3:
            bot.reply_to(message, "⚠️ Использование: /gems [ID] [количество]")
            return
        
        player_id = int(parts[1])
        gems_amount = int(parts[2])
        
        # Ищем игрока по ID
        player_data = db.load_player_account_by_id(player_id)
        if not player_data:
            bot.reply_to(message, f"❌ Игрок с ID {player_id} не найден!")
            return
        
        # Обновляем гемы
        db.update_player_account(player_data['Token'], 'Gems', gems_amount)
        
        bot.reply_to(message, f"✅ Игроку {player_data.get('Name', 'Unknown')} выдано {gems_amount} гемов!")
        
    except Exception as e:
        bot.reply_to(message, f"❌ Ошибка: {str(e)}")

# Команда /players
@bot.message_handler(commands=['players'])
def list_players(message):
    try:
        if message.from_user.id not in ADMIN_IDS:
            bot.reply_to(message, "❌ У вас нет прав для этой команды!")
            return
        
        players = db.load_all_players(None)
        response = "📊 Список игроков:\n\n"
        
        for player in players:
            response += f"👤 {player.get('Name', 'Unknown')} | ID: {player.get('ID', 'N/A')} | 💎: {player.get('Gems', 0)}\n"
        
        bot.reply_to(message, response)
        
    except Exception as e:
        bot.reply_to(message, f"❌ Ошибка: {str(e)}")

# Запуск бота
if __name__ == "__main__":
    print("🤖 Бот запущен...")
    bot.polling(none_stop=True)