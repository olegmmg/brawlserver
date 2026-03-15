from ByteStream.Reader import Reader
from Protocol.Messages.Server.Team.TeamLeftMessage import TeamLeftMessage
from Core.Matchmaking import MatchmakingManager

class TeamLeaveMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        MatchmakingManager.dequeue(self.player.ID)
        TeamLeftMessage(self.client, self.player).send()
