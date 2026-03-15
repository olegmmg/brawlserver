from ByteStream.Writer import Writer

class LeaderboardMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24403
        self.player = player

    def encode(self):
        self.writeVInt(1)#TYPE
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString("RU")

        self.writeVInt(1)#Count Player
        
        self.writeLogicLong(1)
        self.writeVInt(1)
        self.writeVInt(self.player.trophies)#Trophies

        self.writeVInt(1)
        self.writeString("Brawl Stars")#Club Name
        self.writeString(f"{self.player.name}")#Name

        self.writeVInt(9)
        self.writeVInt(28000000 + self.player.profile_icon)
        self.writeVInt(43000000 + self.player.name_color)
        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeString("RU")


