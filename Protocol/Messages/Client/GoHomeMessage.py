from Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage

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
        OwnHomeDataMessage(self.client, self.player).send()