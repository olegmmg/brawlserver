from ByteStream.Writer import Writer

class LobbyInfoMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23457
        self.player = player

    def encode(self):
        self.writeVInt(1)
        self.writeString("Brawl Stars")

        self.writeVInt(0) # array
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
