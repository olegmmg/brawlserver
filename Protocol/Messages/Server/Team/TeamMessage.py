from ByteStream.Writer import Writer

class TeamMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        self.writeVInt(1)#Room type
        self.writeUInt8(0)
        self.writeVInt(1)
        
        self.writeLong(0)
        self.writeUInt8(0)
        self.writeUInt8(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeDataReference(15, 7)

        self.writeVInt(1)
        for x in range(1):

            self.writeVInt(1)#Players Count

            self.writeLong(1)#Low ID

            self.writeDataReference(16, 2)
            self.writeDataReference(29, 0)

            self.writeVInt(99999)
            self.writeVInt(99999)
            self.writeVInt(10)

            self.writeVInt(3)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

            self.writeString(self.player.name)
            self.writeVInt(100)
            self.writeVInt(28000000)
            self.writeVInt(43000000)

            self.writeDataReference(23, 0)
            self.writeDataReference(23, 0)

        self.writeVInt(0)
        for x in range(0):
            pass

        self.writeVInt(0)
        for x in range(0):
            pass

        self.writeUInt8(0)
        if self.player.use_gadget:
            self.writeUInt8(6)
        else:
            self.writeUInt8(0)
