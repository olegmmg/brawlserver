import json
import string
import random
from colorama import Fore

class Helpers:
    connected_clients = {"ClientsCount": 0, "Clients": {}}

    yellow = Fore.YELLOW
    green = Fore.GREEN
    blue = Fore.LIGHTBLUE_EX
    cyan = Fore.CYAN
    red = Fore.RED

    def randomToken(self):
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(40))

    def randomID(self, length = 8):
        return int(''.join([str(random.randint(0, 9)) for _ in range(length)]))

    def create_config(self):
        settings = {
            "Username": "F1ash",
            "Gems": 6666,
            "Gold": 9999,
            "StarPoints": 4444,
            "BrawlBoxTokens": 0,
            "BigBoxTokens": 0,
            "Trophies": 99999,
            "HighestTrophies": 999999,
            "ExperiencePoints": 999999,
            "NameColor": 0,
            "Thumbnail": 0,
            "TrophyRoadReward": 200,
            "Region": "UA",
            "SupportedContentCreator": "F1ash",
            "ThemeID": 0,
            "BrawlersTrophies": 0,
            "BrawlersHighestTrophies": 0,
            "BrawlersPowerPoints": 0,
            "BrawlersLevel": 9,
            "Environment": "dev"
        }


        with open('config.json', 'w') as config_file:
            json.dump(settings, config_file)