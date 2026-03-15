from ByteStream.Reader import Reader
from Core.Matchmaking import MatchmakingManager

class TeamCreateMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.map_slot  = self.readVInt()
        self.map_id    = self.readVInt()
        self.room_type = self.readVInt()

    def process(self):
        self.player.map_id = self.map_id
        MatchmakingManager.enqueue(self.client, self.player)
