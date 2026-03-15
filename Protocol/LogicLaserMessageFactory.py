from Protocol.Messages.Client.ClientHelloMessage import ClientHelloMessage
#Login
from Protocol.Messages.Client.LoginMessage import LoginMessage
#Profile
from Protocol.Messages.Client.GetPlayerProfileMessage import GetPlayerProfileMessage
#LeaderBoard
from Protocol.Messages.Client.GetLeaderboardMessage import GetLeaderboardMessage
#BattleEnd
from Protocol.Messages.Client.AskForBattleEndMessage import AskForBattleEndMessage
#Alliance - ЗАМЕНА ИМПОРТОВ
try:
    from Protocol.Messages.Server.Alliance.AllianceListMessage import AllianceListMessage
    from Protocol.Messages.Server.Alliance.ChangeAllianceSettingsMessage import ChangeAllianceSettingsMessage
except ImportError:
    # Создаем заглушки если файлы не найдены
    class AllianceListMessage:
        def __init__(self, client, player):
            self.client = client
            self.player = player
        def send(self):
            print(f"[AllianceList] Sending alliance list for player {self.player.ID}")
    
    class ChangeAllianceSettingsMessage:
        def __init__(self, client, player):
            self.client = client
            self.player = player
        def send(self):
            print(f"[AllianceSettings] Changing alliance settings for player {self.player.ID}")
#GameRoom
from Protocol.Messages.Server.Team.TeamCreateMessage import TeamCreateMessage
from Protocol.Messages.Server.Team.TeamMessage import TeamMessage

# Добавляем импорт для установки имени
from Protocol.Messages.Client.SetPlayerNameMessage import SetPlayerNameMessage

# Заглушки для необработанных пакетов
class UnhandledMessage:
    def __init__(self, client, player, initial_bytes):
        self.client = client
        self.player = player
        self.initial_bytes = initial_bytes
        
    def decode(self):
        pass
        
    def process(self):
        print(f"[Unhandled] Packet processed but not implemented")
        # Отправляем пустой ответ чтобы клиент не отключался
        try:
            self.client.send(b'\x00' * 7)
        except:
            pass

# Добавляем заглушки для обучения
try:
    from Protocol.Messages.Client.TutorialMessage import TutorialMessage
except ImportError:
    # Заглушки если файлы не найдены
    class TutorialMessage:
        def __init__(self, client, player, initial_bytes):
            self.client = client
            self.player = player
        def decode(self):
            pass
        def process(self):
            print(f"[Tutorial] Player {self.player.ID} tutorial processed")

# Добавляем правильный обработчик для GoHomeMessage
try:
    from Protocol.Messages.Client.GoHomeMessage import GoHomeMessage
except ImportError:
    # Создаем локальную версию если файл не найден
    class GoHomeMessage:
        def __init__(self, client, player, initial_bytes):
            self.client = client
            self.player = player
            self.initial_bytes = initial_bytes
            
        def decode(self):
            pass
            
        def process(self):
            print(f"[GoHome] Player {self.player.ID} going home")
            # Отправляем данные дома при выходе
            try:
                from Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
                OwnHomeDataMessage(self.client, self.player).send()
            except Exception as e:
                print(f"[GoHome] Error sending home data: {e}")

# Специфичные заглушки для часто используемых пакетов
class KeepAliveMessage:
    def __init__(self, client, player, initial_bytes):
        self.client = client
        self.player = player
        
    def decode(self):
        pass
        
    def process(self):
        # Просто отвечаем чтобы поддерживать соединение
        try:
            self.client.send(b'\x00' * 7)
        except:
            pass
        print(f"[KeepAlive] Connection kept alive")

class EndClientTurnMessage:
    def __init__(self, client, player, initial_bytes):
        self.client = client
        self.player = player
        
    def decode(self):
        pass
        
    def process(self):
        print(f"[EndClientTurn] Turn ended")

class ClientCapabilitiesMessage:
    def __init__(self, client, player, initial_bytes):
        self.client = client
        self.player = player
        
    def decode(self):
        pass
        
    def process(self):
        print(f"[ClientCapabilities] Capabilities received")

class VisitHomeMessage:
    def __init__(self, client, player, initial_bytes):
        self.client = client
        self.player = player
        
    def decode(self):
        pass
        
    def process(self):
        print(f"[VisitHome] Home visited")
        # Отправляем данные дома
        try:
            from Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
            OwnHomeDataMessage(self.client, self.player).send()
        except Exception as e:
            print(f"[VisitHome] Error sending home data: {e}")

class ChangeAvatarNameMessage:
    def __init__(self, client, player, initial_bytes):
        self.client = client
        self.player = player
        
    def decode(self):
        pass
        
    def process(self):
        print(f"[ChangeName] Name change requested")

class BindGoogleServiceAccountMessage:
    def __init__(self, client, player, initial_bytes):
        self.client = client
        self.player = player
        
    def decode(self):
        pass
        
    def process(self):
        print(f"[GoogleBind] Google account binding")

class PlayerStatusMessage:
    def __init__(self, client, player, initial_bytes):
        self.client = client
        self.player = player
        
    def decode(self):
        pass
        
    def process(self):
        print(f"[PlayerStatus] Player status update")

packets = {
    # Основные пакеты
    10100: ClientHelloMessage,
    10101: LoginMessage,
    14113: GetPlayerProfileMessage,
    14403: GetLeaderboardMessage,
    14110: AskForBattleEndMessage,
    24310: AllianceListMessage,
    24124: TeamMessage,
    20300: SetPlayerNameMessage,
    10110: TutorialMessage,
    10108: GoHomeMessage,
    
    # Keep Alive пакеты
    19004: KeepAliveMessage,
    10111: KeepAliveMessage,
    
    # Клиентские возможности
    30000: ClientCapabilitiesMessage,
    
    # Игровые пакеты
    10113: EndClientTurnMessage,
    14134: VisitHomeMessage,
    14212: ChangeAvatarNameMessage,
    14211: BindGoogleServiceAccountMessage,
    12951: PlayerStatusMessage,
    
    # Общая заглушка для других пакетов
    19888: UnhandledMessage,
}


class LogicLaserMessageFactory:
    def __init__(self, client, player):
        self.client = client
        self.player = player

    def processMessage(self, payload, messageID):
        if messageID in packets:
            message = packets[messageID](self.client, self.player, payload)
            
            if hasattr(message, 'decode'):
                message.decode()
            
            if hasattr(message, 'process'):
                message.process()
        else:
            print(f"[LogicLaserMessageFactory] Unknown message ID: {messageID}")
            # Для неизвестных пакетов используем общую заглушку
            message = UnhandledMessage(self.client, self.player, payload)
            message.process()
