from ByteStream.Writer import Writer


class BattleLogMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23458
        self.player = player

    def encode(self):
        self.writeBoolean(True)

        self.writeVInt(1)  # Count

        for x in range(1):
            self.writeVInt(0)
            self.writeVInt(228)  # Time When Battle Log Entry Was Created
            self.writeVInt(1)  # Battle Log Type (1 = Normal, 2 = Crash, 3 = Survived for <time>,
            self.writeVInt(228)  # Trophies Result
            self.writeVInt(1313)  # Battle Time
            self.writeUInt8(1)  # Type [0 = Power Play, 1 = Friendly, 2 = Championship]
            self.writeDataReference(15, 96)  # Map SCID
            self.writeVInt(0)  # Victory/Defeat/Draw
            self.writeVInt(0)  # ???

            self.writeInt(2)
            self.writeInt(2)

            self.writeVInt(1)
            self.writeUInt8(1)

            self.writeVInt(0)  # array

        self.writeVInt(0)
        self.writeUInt8(0)
        self.writeVInt(0)
        self.writeUInt8(0)
        self.writeVInt(0)
