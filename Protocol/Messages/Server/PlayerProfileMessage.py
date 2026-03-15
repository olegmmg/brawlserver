from ByteStream.Writer import Writer


class PlayerProfileMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24113
        self.player = player

    def encode(self):
        self.writeVInt(0)#High ID
        self.writeVInt(1)#Low ID

        self.writeVInt(0)#?

        self.writeVInt(1)
        self.writeScId(16, 0)
        self.writeVInt(0)
        self.writeVInt(1250)  # Trophies for rank
        self.writeVInt(1250)  # Trophies
        self.writeVInt(9)  # power lvl

        self.writeVInt(6)#Count Array

        self.writeVInt(4)  # ID
        self.writeVInt(self.player.high_trophies)  # Highest Trophies
        
        self.writeVInt(3)  # ID
        self.writeVInt(self.player.trophies)  # Trophies
        
        self.writeVInt(5)  # ID
        self.writeVInt(1)  # Brawlers List
        
        self.writeVInt(15)  # ID
        self.writeVInt(15)  # Challenge Wins
        
        self.writeVInt(17)  # ID
        self.writeVInt(19)  # Power League Rank  Team
        
        self.writeVInt(18)  # ID
        self.writeVInt(19)  # Power League Rank Team

        # sub_64DF74
        self.writeString(f"{self.player.name}")
        self.writeVInt(100)
        self.writeVInt(28000000 + self.player.profile_icon)#Icon
        self.writeVInt(43000000 + self.player.name_color)#Name Color
        self.writeVInt(46000000)
        
        self.writeBoolean(True)  # Is in club

        self.writeInt(0)
        self.writeInt(1)
        self.writeString("Brawl Stars")  # club name
        self.writeVInt(8)
        self.writeVInt(2)  # Club badgeID
        self.writeVInt(1)  # club type | 1 = Open, 2 = invite only, 3 = closed
        self.writeVInt(1)  # Current members count
        self.writeVInt(0)
        self.writeVInt(0)  # Trophy required
        self.writeVInt(0)  # (Unknown)
        self.writeString("RU")  # region
        self.writeVInt(0)  # (Unknown)
        self.writeVInt(0)  # (Unknown)
        self.writeVInt(25)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeVInt(0)