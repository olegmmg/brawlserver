from ByteStream.Writer import Writer

class AllianceStreamMessage(Writer):

    def __init__(self, client, player, db):
        super().__init__(client)
        self.id = 24311
        self.player = player
        self.db = db


    def encode(self):
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeLogicLong(1)
        self.writeString("Penis")
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeVInt(0)

