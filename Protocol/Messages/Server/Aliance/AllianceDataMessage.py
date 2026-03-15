from ByteStream.Writer import Writer

class AllianceDataMessage(Writer):

    def __init__(self, client, player, db):
        super().__init__(client)
        self.id = 24301
        self.player = player
        self.db = db

    def encode(self):
        self.writeVInt(1)
        
        self.writeLong(0)
        self.writeLong(1)
        self.writeString("<cff3200>v<cff6500>a<cff9800>n<cffcb00>y<cffff00>a<cffff00>_<cccff00>d<c99ff00>e<c66ff00>v</c>") # Club Name
        self.writeDataReference(8, 0)
        self.writeVInt(1) # Type
        self.writeVInt(1)  # Total Members
        self.writeVInt(1)  # Total Trophies
        self.writeVInt(1)  # Trophies Required
        self.writeDataReference(0)
        self.writeString("RU")  # Region
        self.writeVInt(0)
        self.writeBoolean(0)  # Family Friendly
        self.writeVInt(0)

        self.writeString("Pedil") # Description

        self.writeVInt(1) # Members Count

        self.writeLong(0)
        self.writeLong(1)
        self.writeVInt(2) # Role
        self.writeVInt(1) # Trophies
        self.writeVInt(2) # Player State TODO: Members state
        self.writeVInt(0) # State Timer

        self.writeBoolean(False) # DoNotDisturb TODO: Do not disturb sync

        self.writeString("Ponbbhhh") # Player Name
        self.writeVInt(100)
        self.writeVInt(28000000) # Player Thumbnail
        self.writeVInt(43000000) # Player Name Color
        self.writeVInt(-1) # Player Brawlpass Name

        self.writeVInt(-1)
        self.writeBoolean(False)