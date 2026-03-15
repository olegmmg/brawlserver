from ByteStream.Reader import Reader
from Protocol.Messages.Server.LoginOkMessage import LoginOkMessage
from Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
#Aliance
from Protocol.Messages.Server.Aliance.AllianceDataMessage import AllianceDataMessage
from Protocol.Messages.Server.Aliance.MyAllianceMessage import MyAllianceMessage
from Protocol.Messages.Server.Aliance.AllianceStreamMessage import AllianceStreamMessage
#Lobby
from Lobby.MaintenceMessage import MaintenceMessage
from Lobby.WarMessage import WarMessage
#Friend
from Protocol.Messages.Server.Friends.FriendMessage import FriendMessage

# Database
try:
    from Database.DatabaseManager import DB as DataBase
except ImportError:
    class DataBase:
        def __init__(self):
            pass
        def load_player_account(self, id, token):
            return {'Name': '', 'NameSet': False, 'Trophies': 0, 'Gems': 0}
        def set_player_name(self, token, name):
            print(f"Would set name: {name}")
        def load_all_players(self, args):
            return []

class LoginMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.db = DataBase()

    def decode(self):
        pass

    def process(self):
        try:
            # Загружаем данные игрока
            player_data = self.db.load_player_account(self.player.ID, self.player.token)
            
            # Проверяем, установлено ли имя
            if not player_data or not player_data.get('Name') or player_data['Name'] == '' or not player_data.get('NameSet', False):
                # Автогенерация имени: Player 1, Player 2, etc.
                all_players = self.db.load_all_players(None)
                player_number = len(all_players) + 1
                generated_name = f"Player {player_number}"
                
                # Сохраняем сгенерированное имя
                self.db.set_player_name(self.player.token, generated_name)
                player_data = self.db.load_player_account(self.player.ID, self.player.token)
                print(f"[Login] Auto-generated name: {generated_name}")
            
            # Обновляем данные игрока в объекте player
            self._update_player_data(player_data)
            # Завершаем вход
            self._complete_login(player_data)
                
        except Exception as e:
            print(f"Login error: {e}")
            self._send_basic_packets()

    def _update_player_data(self, player_data):
        if player_data:
            self.player.name = player_data.get('Name', self.player.name)
            self.player.trophies = player_data.get('Trophies', self.player.trophies)
            self.player.high_trophies = player_data.get('HighestTrophies', self.player.high_trophies)
            self.player.gems = player_data.get('Gems', self.player.gems)
            self.player.exp_points = player_data.get('ExperiencePoints', self.player.exp_points)

    def _complete_login(self, player_data):
        self._update_player_data(player_data)
        self._send_all_packets()

    def _send_basic_packets(self):
        try:
            LoginOkMessage(self.client, self.player).send()
            OwnHomeDataMessage(self.client, self.player).send()
        except Exception as e:
            print(f"Error sending basic packets: {e}")

    def _send_all_packets(self):
        try:
            LoginOkMessage(self.client, self.player).send()
            OwnHomeDataMessage(self.client, self.player).send()
            
            # Aliance
            AllianceDataMessage(self.client, self.player, self.db).send()
            MyAllianceMessage(self.client, self.player, self.db).send()
            AllianceStreamMessage(self.client, self.player, self.db).send()
            
            # Lobby
            FriendMessage(self.client, self.player).send()
            WarMessage(self.client, self.player).send()
            
            print(f"[Login] Player {self.player.name} logged in successfully")
            
        except Exception as e:
            print(f"Error sending login packets: {e}")
            self._send_basic_packets()