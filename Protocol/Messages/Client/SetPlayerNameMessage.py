# Protocol/Messages/Client/SetPlayerNameMessage.py
from ByteStream.Reader import Reader
from Protocol.Messages.Server.LoginOkMessage import LoginOkMessage
from Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage

# Исправляем импорт
try:
    from Database.DatabaseManager import DB as DataBase
except ImportError:
    # Заглушка на случай ошибки
    class DataBase:
        def __init__(self):
            pass
        def set_player_name(self, token, name):
            print(f"Would set name: {name}")
        def load_player_account(self, id, token):
            return {'Name': 'Player', 'Trophies': 0}

class SetPlayerNameMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.db = DataBase()

    def decode(self):
        self.playerName = self.readString()  # Читаем введенное имя

    def process(self):
        # Проверяем валидность имени
        if len(self.playerName) < 2 or len(self.playerName) > 15:
            # Если имя невалидно, снова запрашиваем
            from Protocol.Messages.Server.AskForPlayerNameMessage import AskForPlayerNameMessage
            AskForPlayerNameMessage(self.client, self.player).send()
            return
        
        # Сохраняем имя в базу данных
        self.db.set_player_name(self.player.token, self.playerName)
        
        # Обновляем имя в объекте игрока
        self.player.name = self.playerName
        
        # Отправляем пакеты успешного входа
        LoginOkMessage(self.client, self.player).send()
        OwnHomeDataMessage(self.client, self.player).send()