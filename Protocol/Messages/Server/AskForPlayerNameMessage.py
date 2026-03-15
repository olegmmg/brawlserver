from ByteStream.Writer import Writer

class AskForPlayerNameMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20300
        self.player = player

    def encode(self):
        self.writeInt(1)  # State: 1 = требуется ввод имени
        self.writeString("")  # Пустая строка
        self.writeInt(0)   # Unknown