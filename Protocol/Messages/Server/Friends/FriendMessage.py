from ByteStream.Writer import Writer
from Lobby.MaintenceMessage import MaintenceMessage

class FriendMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20199
        self.player = player

    def encode(self):
    	pass

    