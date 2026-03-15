from ByteStream.Writer import Writer

class AllianceListMessage(Writer):

    def __init__(self, client, player, query, clubs):
        super().__init__(client)
        self.id = 24310
        self.player = player
        self.query = query
        self.clubs = clubs

    def encode(self):

        self.writeString(self.query)

        self.writeVInt(1)

        self.writeLong(1)
        self.writeString("Wat1rX")
        self.writeDataReference(8, 1)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(10)
        self.writeVInt(10)
        self.writeDataReference(0,0)
        self.writeString("RU")
        self.writeVInt(0)
        self.writeVInt(0)