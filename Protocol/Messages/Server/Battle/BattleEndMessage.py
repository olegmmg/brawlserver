from ByteStream.Writer import Writer


class BattleEndMessage(Writer):

    def __init__(self, client, player, type, result, players):
        super().__init__(client)
        self.id = 23456
        self.player  = player
        self.type    = type
        self.result  = result
        self.players = players

    def encode(self):
        self.writeVInt(5)#Game Mode Type
        self.writeVInt(self.result)#Result
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)

        self.writeVInt(0)
        self.writeVInt(32)#Battle End Result
        self.writeVInt(0)#?
        self.writeBoolean(False)

       # Players Array
        self.writeVInt(2) # Battle End Screen Players
        self.writeVInt(1) # Player Team and Star Player Type
        self.writeScId(16, 1) # Player Brawler
        self.writeScId(29, 0) # Player Skin
        self.writeVInt(0) # Brawler Trophies
        self.writeVInt(0) # Player Power Play Points
        self.writeVInt(0) # Brawler Power Level
        self.writeBoolean(True) # Player HighID and LowID Array
        self.writeInt(0) # HighID
        self.writeInt(1) # LowID
        self.writeString("Name") # Player Name
        self.writeVInt(0) # Player Experience Level
        self.writeVInt(28000000) # Player Profile Icon
        self.writeVInt(43000000) # Player Name Color
        self.writeVInt(0) # Null VInt
        
        self.writeVInt(1) # Player Team and Star Player Type
        self.writeScId(16, 1) # Player Brawler
        self.writeScId(29, 0) # Player Skin
        self.writeVInt(0) # Brawler Trophies
        self.writeVInt(0) # Player Power Play Points
        self.writeVInt(0) # Brawler Power Level
        self.writeBoolean(True) # Player HighID and LowID Array
        self.writeInt(0) # HighID
        self.writeInt(1) # LowID
        self.writeString("Name") # Player Name
        self.writeVInt(0) # Player Experience Level
        self.writeVInt(28000000) # Player Profile Icon
        self.writeVInt(43000000) # Player Name Color
        self.writeVInt(0) # Null VInt
        
        self.writeScId(28, 0)  # Player Profile Icon
        self.writeBoolean(True)  # Play Again