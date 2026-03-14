from ByteStream.Reader import Reader
from Logic.Home.LogicEventData import LogicEventData
from Core.Matchmaking import MatchmakingManager

class StartGameMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.map_slot = self.readVInt()

    def process(self, db):
        self.player.map_id = LogicEventData.events[self.map_slot - 1]['ID']
        MatchmakingManager.enqueue(self.client, self.player)
