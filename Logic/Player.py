import json
from Utils.Helpers import Helpers
from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Skins import Skins
from Files.CsvLogic.Cards import Cards

class Player:
    try:
        config = open('config.json', 'r')
        content = config.read()
    except FileNotFoundError:
        Helpers().create_config()
        config = open('config.json', 'r')
        content = config.read()

    settings = json.loads(content)

    skins_id = Skins().get_skins_id()
    brawlers_id = Characters().get_brawlers_id()

    ID = 1
    token = 'SomeRandomToken'

    name = settings['Username']
    profile_icon = settings['Thumbnail']
    name_color = settings['NameColor']
    trophies = settings['Trophies']
    high_trophies = settings['HighestTrophies']
    trophy_reward = settings['TrophyRoadReward']
    exp_points = settings['ExperiencePoints']
    gems = 0  # Гемы обнулены
    resources = [
        {'ID': 1, 'Amount': settings['BrawlBoxTokens']},  # Обычные ящики
        {'ID': 8, 'Amount': settings['Gold']},            # Золото
        {'ID': 9, 'Amount': 3},                          # 3 мега ящика (BigBoxTokens)
        {'ID': 10, 'Amount': settings['StarPoints']}     # Звездные очки
    ]
    region = settings['Region']
    content_creator = settings['SupportedContentCreator']
    theme_id = settings['ThemeID']
    environment = settings['Environment']

    db = None

    # ТОЛЬКО ШЕЛЛИ РАЗБЛОКИРОВАН (ID: 0)
    unlocked_skins = []  # Все скины закрыты
    brawlers_unlocked = [0]  # Только Шелли разблокирован

    brawlers_card_id = []
    for x in brawlers_unlocked:
        brawlers_card_id.append(Cards().get_unlock_by_brawler_id(x))

    brawlers_spg = Cards().get_spg_id()

    def_trophies = settings['BrawlersTrophies']
    def_high_trophies = settings['BrawlersHighestTrophies']

    brawlers_trophies = {}
    for x in brawlers_id:
        brawlers_trophies.update({f'{x}': def_trophies})

    brawlers_high_trophies = {}
    for x in brawlers_id:
        brawlers_high_trophies.update({f'{x}': def_high_trophies})

    def_level = settings['BrawlersLevel'] - 1

    brawlers_level = {}
    for x in brawlers_id:
        brawlers_level.update({f'{x}': def_level})

    def_pp = settings['BrawlersPowerPoints']

    brawlers_powerpoints = {}
    for x in brawlers_id:
        brawlers_powerpoints.update({f'{x}': def_pp})

    clients = {}

    def __init__(self, device, db=None):
        self.device = device
        self.db = db
        # При необходимости можно загрузить данные из БД
        if db is not None:
            self.load_from_db()

    def load_from_db(self):
        """Загружает данные игрока из базы данных"""
        if self.db is not None:
            # Здесь код для получения данных игрока из БД
            # Например:
            # player_data = self.db.get_player_data(self.ID)
            # if player_data:
            #     self.update_from_db(player_data)
            pass

    def update_from_db(self, player_data):
        """Обновляет данные игрока из базы данных"""
        if player_data:
            self.name = player_data.get('Name', self.name)
            self.trophies = player_data.get('Trophies', self.trophies)
            self.high_trophies = player_data.get('HighestTrophies', self.high_trophies)
            self.gems = player_data.get('Gems', self.gems)
            self.exp_points = player_data.get('ExperiencePoints', self.exp_points)
            self.profile_icon = player_data.get('ProfileIcon', self.profile_icon)
            self.name_color = player_data.get('NameColor', self.name_color)