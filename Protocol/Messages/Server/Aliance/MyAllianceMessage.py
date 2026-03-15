from ByteStream.Writer import Writer

class MyAllianceMessage(Writer):

    def __init__(self, client, player, db):
        super().__init__(client)
        self.id = 24399
        self.player = player
        self.db = db

    def encode(self):
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeDataReference(25, 2)
        self.writeLong(1)
        self.writeString("Name")
        self.writeDataReference(8, 2)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(1)#Trophies
        self.writeVInt(1)
        self.writeDataReference(0, 0)
        self.writeString("RU")
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

