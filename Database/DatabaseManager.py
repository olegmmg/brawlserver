import sys
import os
import datetime
import json
from Utils.Helpers import Helpers

# Добавляем пути для импортов
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

try:
    from SQLManager import DataBase as dB
    from Logic.Player import Player
except ImportError:
    # Альтернативный импорт если первый не работает
    import importlib.util
    spec = importlib.util.spec_from_file_location("SQLManager", os.path.join(current_dir, "SQLManager.py"))
    SQLManager = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(SQLManager)
    dB = SQLManager.DataBase
    
    spec = importlib.util.spec_from_file_location("Player", os.path.join(parent_dir, "Logic", "Player.py"))
    PlayerModule = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(PlayerModule)
    Player = PlayerModule.Player

class DB:
    def __init__(self):
        self.player = Player
        # Создаем папки если их нет
        os.makedirs("Database/Player", exist_ok=True)
        os.makedirs("Database/Club", exist_ok=True)
        
        self.client = dB("Database/Player/player.db")
        self.clubs = dB("Database/Club/club.db")

        self.data = {
            'Name': '',  # Пустое имя вместо "Guest"
            'NameSet': False,  # Имя еще не установлено
            'Gems': getattr(Player, 'gems', 0),
            'Trophies': getattr(Player, 'trophies', 0),
            'Resources': getattr(Player, 'resources', []),
            'TokenDoubler': 1000,
            'HighestTrophies': 0,
            'HomeBrawler': 49,
            'TrophyRoadReward': 195,
            'ExperiencePoints': getattr(Player, 'exp_points', 0),
            'ProfileIcon': 0,
            'NameColor': 0,
            'BrawlersTrophies': 0,
            'BrawlersHighestTrophies': 0,
            'BrawlersLevel': 9,
            'BrawlersPowerPoints': 0,
            'SelectedBrawler': 49,
            'Region': getattr(Player, 'region', 'RU'),
            'SupportedContentCreator': "F1ash",
            'ClubID': 0,
            'ClubRole': 1,
        }

        self.club_data = {
            'Name': '',
            'Description': '',
            'Region': 'RU',
            'BadgeID': 0,
            'Type': 0,
            'Trophies': 0,
            'RequiredTrophies': 0,
            'FamilyFriendly': 0,
            'Members': [],
            'Messages': ["By F1ash"]
        }

    def merge(self, dict1, dict2):
        return dict1.update(dict2)

    def create_player_account(self, id, token):
        auth = {
            'ID': id,
            'Token': token,
        }

        auth.update(self.data.copy())
        self.client.insert(token, auth)

    def load_player_account(self, id, token):
        result = self.client.load_data(token)
        if result:
            for x in self.data:
                if x not in result:
                    result[x] = self.data[x]
            return result
        else:
            # Если аккаунт не найден, создаем новый
            self.create_player_account(id, token)
            return self.load_player_account(id, token)

    def load_player_account_by_id(self, id):
        collections = self.client.load_all()
        for collection in collections:
            if collection.get("ID") == id:
                return collection
        return None

    def update_player_account(self, token, item, value):
        self.client.update(token, item, value)

    def set_player_name(self, token, name):
        """Метод для установки имени игрока"""
        self.client.update(token, 'Name', name)
        self.client.update(token, 'NameSet', True)

    def is_name_available(self, name):
        """Проверяет, доступно ли имя"""
        if not name or len(name) < 2:
            return False
            
        players = self.load_all_players(None)
        for player in players:
            if player.get('Name') == name:
                return False
        return True

    def update_all_players(self, query, item, value):
        collections = self.client.load_all()
        for collection in collections:
            self.client.update(collection.get("Token"), item, value)
            
    def load_all_players(self, args):
        result = self.client.load_all()
        return result if result else []

    def load_all_players_sorted(self, args, element):
        result = self.client.load_all()
        if result:
            sorter = sorted(result, key=lambda x: x.get(element, 0), reverse=True)
            return sorter
        return []

    def create_club(self, id, data):
        auth = {
            'ID': id,
        }
        auth.update(data)
        self.clubs.insert(id, auth)

    def update_club(self, id, item, value):
        self.clubs.update(id, item, value)

    def load_club(self, id):
        result = self.clubs.load_data(id)
        return result

    def load_all_clubs_sorted(self, args, element):
        result = self.clubs.load_all()
        if result:
            sorter = sorted(result, key=lambda x: x.get(element, 0), reverse=True)
            return sorter
        return []

    def load_all_clubs(self, args):
        result = self.clubs.load_all()
        return result if result else []

    def delete_club(self, id):
        self.clubs.delete(id)

    def close(self):
        self.client.close()
        self.clubs.close()


# Для тестирования
if __name__ == "__main__":
    db = DB()
    print("DatabaseManager loaded successfully!")
