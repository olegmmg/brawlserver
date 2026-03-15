from ByteStream.Writer import Writer


class LoginOkMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 20104

    def encode(self):
        self.writeLong(self.player.ID)
        self.writeLong(self.player.ID)

        self.writeString(self.player.token)
        self.writeString()
        self.writeString()

        self.writeInt(34)  # MajorVersion
        self.writeInt(151)  # Build
        self.writeInt(1)  # MinorVersion

        self.writeString(self.player.environment)

        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)

        self.writeString()
        self.writeString()
        self.writeString()

        self.writeInt(0)

        self.writeString()
        self.writeString(self.player.region)
        self.writeString()

        self.writeInt(1)
        self.writeString()

        self.writeInt(2)
        self.writeString()
        self.writeString()

        self.writeInt(1)
        self.writeString()
        
        # Добавляем отправку имени игрока
        self.writeString(self.player.name)  # ← ВАЖНО: отправляем имя игрока