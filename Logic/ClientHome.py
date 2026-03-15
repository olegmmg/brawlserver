import json
from datetime import datetime


class LogicClientHome:

    def encode(self):
        time_stamp = int(datetime.timestamp(datetime.now()))

        self.writeVInt(time_stamp)
        self.writeVInt(time_stamp)

        self.writeVInt(self.player.trophies)#trophies
        self.writeVInt(self.player.high_trophies)#max trophies
        self.writeVInt(self.player.high_trophies)#max trophies

        self.writeVInt(self.player.trophy_reward)#trophy road
        self.writeVInt(self.player.exp_points)#exp

        self.writeDataReference(28, self.player.profile_icon)#profile icon
        self.writeDataReference(43, self.player.name_color)#Name Color

        self.writeVInt(50)#Brawlers?
        for x in range(50):
            self.writeVInt(x)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(len(self.player.unlocked_skins))
        for x in self.player.unlocked_skins:
            self.writeDataReference(29, x)
            #Unlocked skins array end

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)
            #?

        self.writeVInt(0)#?
        self.writeVInt(0)#?
        self.writeVInt(1)#?
        self.writeVInt(1)#?

        self.writeBoolean(False)#Boolean
        
        self.writeVInt(0)#?
        self.writeVInt(0)#?
        self.writeVInt(360000)#Trophy Road Timer
        self.writeVInt(3600000)#Brawl Pass Timer

        self.writeBoolean(False)#Boolean 1
        self.writeBoolean(False)#Boolean 2

        self.writeUInt8(0)
        self.writeVInt(0)
        self.writeVInt(4)#Shop Token Doublr
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(2)

        self.writeVInt(0)#?

        events = json.loads(open("shop.json", "r").read())
        
        self.writeVInt(1) # Offers Count
        
        self.writeVInt(1) # Item Count
        
        self.writeVInt(9) # ItemType
        self.writeVInt(100) # Amount
        self.writeDataReference(0, 0) # CsvID
        self.writeVint(22) # SkinID
        
        self.writeVInt(0) # Currency
        self.writeVInt(59) # Cost
        self.writeVInt(99999) # Time
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # Claimed
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # DailyOffer
        self.writeVInt(79) # OldPrice
        self.writeInt(0)
        self.writeString("t.me/BGJSTUDIO") # Offer Text
        self.writeVInt(0)
        self.writeString("offer_punk") # Background
        self.writeVInt(0)
        self.writeBoolean(False) # Processing
        self.writeVInt(1) # TypeBenefit
        self.writeVInt(2) # Benefit
        self.writeBoolean(False) # Array

        self.writeVInt(20)#Tokens
        self.writeVInt(20)#Timer

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)#Tickets

        self.writeDataReference(16, 0)

        self.writeString(self.player.region)
        self.writeString(self.player.content_creator)

        self.writeBoolean(True)#Boolean
        self.writeInt(4)#anim id
        self.writeInt(0)#Count

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeBoolean(True)
        for x in range(1):
            self.writeVInt(6)#Season
            self.writeVInt(34500)#Tokens
            self.writeBoolean(True)#Buy Brawl Pass
            self.writeVInt(34500)
            self.writeUInt8(0)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        quests = json.loads(open("quests.json", 'r').read()) # import json
        self.writeBoolean(True) # LogicQuests
        self.writeVInt(len(quests)) # Quests Count
        for x in range(1):
        		for quests in quests:
        			self.writeVInt(2)     # Unknown
        			self.writeVInt(2)     # Unknown
        			self.writeVInt(quests['MissionType'])     # Mission Type
        			self.writeVInt(quests['AchievedGoal'])     # Achieved Goal
        			self.writeVInt(quests['QuestGoal'])     # Quest Goal
        			self.writeVInt(quests['TokensReward'])    # Tokens Reward
        			self.writeVInt(2)     # Unknown
        			self.writeVInt(quests['CurrentLevel'])     # Current level
        			self.writeVInt(quests['MaxLevel'])     # Max level
        			self.writeVInt(quests['Timer'])     # Timer
        			self.writeInt8(quests['QuestState'])    # Quest State
        			self.writeDataReference(16, quests['BrawlerID']) # Brawler(16, <BrawlerID>)
        			self.writeVInt(quests['GameMode'])     # GameMode
        			self.writeVInt(2)     # Unknown
        			self.writeVInt(2)     # Unknown
        			self.writeVInt(2)     # Unknown

        self.writeBoolean(True) #Иконки, эмодзи
        self.writeVInt(520)
        for i in range(520):
        	self.writeDataReference(52, i)
        	self.writeVInt(1)
        	self.writeVInt(1)
        	self.writeVInt(1)

        self.writeBoolean(True) # Power League Array
        # Power League Data Array Start #
        self.writeVInt(3) # Season
        self.writeVInt(1) # Rank Solo League
        self.writeVInt(3) # Season
        self.writeVInt(19) # Rank Team League
        self.writeVInt(1)#?
        self.writeVInt(19)#Max Rank Solo
        self.writeVInt(1)#Max Rank Team
        self.writeVInt(1)#?
        self.writeVInt(1)#?
        self.writeVInt(1)#Played Game League
        self.writeVInt(0)
        self.writeVInt(0)
        # Power League Data Array End #

        self.writeInt(0)

        self.writeVInt(0)

        self.writeVInt(20)
        for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24]:
            self.writeVInt(x)

        events = json.loads(open("events.json", "r").read())

        self.writeVInt(len(events) + 3)

        for event in events:
            self.writeVInt(0)
            self.writeVInt(events.index(event) + 1) # EventType
            self.writeVInt(event['CountdownTimer']) # Events Begin Countdown
            self.writeVInt(event['Timer']) # Timer
            self.writeVInt(event['TokensReward']) # Tokens reward for new event
            self.writeDataReference(15, event['ID']) # MapID
            self.writeVInt(-64) # Gamemode Variation
            self.writeVInt(event['Status']) # State
            self.writeString()
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            if event['Modifier'] > 0:
                self.writeBoolean(True)
                self.writeVInt(event['Modifier'])
            else:
                self.writeBoolean(False)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False) # Mapmaker Map Structure
            self.writeVInt(0)
            self.writeBoolean(False) # Power League Data Array
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False) # ChronosTextEntry
            self.writeVInt(0) # Array
            self.writeVInt(0) # Array	

        # Championship Challenge Start Array #
        # Championship Stage 1 #
        self.writeVInt(0)
        self.writeVInt(20) # EventType
        self.writeVInt(0) # Events Begin Countdown
        self.writeVInt(180000) # Timer
        self.writeVInt(0) # Tokens reward for new event
        self.writeDataReference(15, 10) # MapID
        self.writeVInt(-64) # Gamemode Variation
        self.writeVInt(2) # State
        self.writeString("Negr") # ?
        self.writeVInt(0) # ?
        self.writeVInt(0) # Defeats?
        self.writeVInt(15) # Wins in Event Choose
        self.writeBoolean(False) # Modifiers Array
        self.writeVInt(0) # Wins
        self.writeVInt(6) # Modifier Data Array
        self.writeBoolean(False) # Mapmaker Map Structure
        self.writeVInt(0) # Defeats
        self.writeBoolean(False) # Power League Data Array
        self.writeVInt(15) # Total Wins
        self.writeVInt(0) # ?
        self.writeBoolean(False) # ChronosTextEntry
        self.writeBoolean(False) # Array
        self.writeBoolean(False) # Array
        
        # Power League Start Array #
        # Power League Solo Mode #
        self.writeVInt(0)
        self.writeVInt(14) # EventType
        self.writeVInt(0) # Events Begin Countdown
        self.writeVInt(999999) # Timer
        self.writeVInt(0) # Tokens reward for new event
        self.writeDataReference(0,0) # MapID
        self.writeVInt(-64) # Gamemode Variation
        self.writeVInt(2) # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # Mapmaker Map Structure
        self.writeVInt(0)
        self.writeBoolean(True) # Power League Data Array
        # Power League Data Array Start #
        self.writeVInt(3) # Season
        self.writeString("TID_BRAWL_PASS_SEASON_6") # Name Season
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(3) # Quests Count
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(3) # Quest Type
        self.writeVInt(25) # Wins need
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(69) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(2) # Quest Type
        self.writeVInt(7) # Rank
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(70) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(3) # Quest Type
        self.writeVInt(50) # Wins need
        self.writeVInt(1) # Item Array
        self.writeVInt(26) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(307) # SkinID
        
        self.writeVInt(19) # Road Count
        
        self.writeVInt(1) # Rank
        self.writeVInt(500) # Starpoints
        self.writeVInt(2) # Rank
        self.writeVInt(1000) # Starpoints
        self.writeVInt(3)  # Rank
        self.writeVInt(2000) # Starpoints
        self.writeVInt(4)  # Rank
        self.writeVInt(2500) # Starpoints
        self.writeVInt(5)  # Rank
        self.writeVInt(3000) # Starpoints
        self.writeVInt(6)  # Rank
        self.writeVInt(3750) # Starpoints
        self.writeVInt(7)  # Rank
        self.writeVInt(4500) # Starpoints
        self.writeVInt(8)  # Rank
        self.writeVInt(5500) # Starpoints
        self.writeVInt(9)  # Rank
        self.writeVInt(7000) # Starpoints
        self.writeVInt(10)  # Rank
        self.writeVInt(8750) # Starpoints
        self.writeVInt(11)  # Rank
        self.writeVInt(10000) # Starpoints
        self.writeVInt(12)  # Rank
        self.writeVInt(12500) # Starpoints
        self.writeVInt(13)  # Rank
        self.writeVInt(15000) # Starpoints
        self.writeVInt(14)  # Rank
        self.writeVInt(17500) # Starpoints
        self.writeVInt(15)  # Rank
        self.writeVInt(20000) # Starpoints
        self.writeVInt(16)  # Rank
        self.writeVInt(25000) # Starpoints
        self.writeVInt(17)  # Rank
        self.writeVInt(30000) # Starpoints
        self.writeVInt(18)  # Rank
        self.writeVInt(40000) # Starpoints
        self.writeVInt(19)  # Rank
        self.writeVInt(50000) # Starpoints
        # Power League Data Array End #
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # ChronosTextEntry
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array	
        
        # Power League Team Mode #
        self.writeVInt(0)
        self.writeVInt(15) # EventType
        self.writeVInt(0) # Events Begin Countdown
        self.writeVInt(999999) # Timer
        self.writeVInt(0) # Tokens reward for new event
        self.writeDataReference(0,0) # MapID
        self.writeVInt(-64) # Gamemode Variation
        self.writeVInt(2) # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # Mapmaker Map Structure
        self.writeVInt(0)
        self.writeBoolean(True) # Power League Data Array
        # Power League Data Array Start #
        self.writeVInt(3) # Season
        self.writeString("TID_BRAWL_PASS_SEASON_6") # Name Season
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(3) # Quests Count
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(3) # Quest Type
        self.writeVInt(25) # Wins need
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(69) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(2) # Quest Type
        self.writeVInt(7) # Rank
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(70) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(3) # Quest Type
        self.writeVInt(50) # Wins need
        self.writeVInt(1) # Item Array
        self.writeVInt(26) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(307) # SkinID
        
        self.writeVInt(19) # Road Count
        
        self.writeVInt(1) # Rank
        self.writeVInt(500) # Starpoints
        self.writeVInt(2) # Rank
        self.writeVInt(1000) # Starpoints
        self.writeVInt(3)  # Rank
        self.writeVInt(2000) # Starpoints
        self.writeVInt(4)  # Rank
        self.writeVInt(2500) # Starpoints
        self.writeVInt(5)  # Rank
        self.writeVInt(3000) # Starpoints
        self.writeVInt(6)  # Rank
        self.writeVInt(3750) # Starpoints
        self.writeVInt(7)  # Rank
        self.writeVInt(4500) # Starpoints
        self.writeVInt(8)  # Rank
        self.writeVInt(5500) # Starpoints
        self.writeVInt(9)  # Rank
        self.writeVInt(7000) # Starpoints
        self.writeVInt(10)  # Rank
        self.writeVInt(8750) # Starpoints
        self.writeVInt(11)  # Rank
        self.writeVInt(10000) # Starpoints
        self.writeVInt(12)  # Rank
        self.writeVInt(12500) # Starpoints
        self.writeVInt(13)  # Rank
        self.writeVInt(15000) # Starpoints
        self.writeVInt(14)  # Rank
        self.writeVInt(17500) # Starpoints
        self.writeVInt(15)  # Rank
        self.writeVInt(20000) # Starpoints
        self.writeVInt(16)  # Rank
        self.writeVInt(25000) # Starpoints
        self.writeVInt(17)  # Rank
        self.writeVInt(30000) # Starpoints
        self.writeVInt(18)  # Rank
        self.writeVInt(40000) # Starpoints
        self.writeVInt(19)  # Rank
        self.writeVInt(50000) # Starpoints
        # Power League Data Array End #
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # ChronosTextEntry
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        # Power League End Array #

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(0)
        self.writeArrayVint([20, 50, 140, 280])
        self.writeArrayVint([150, 400, 1200, 2600])

        self.writeUInt8(0)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(1)
        for x in range(1):
            self.writeInt(1)
            self.writeInt(41000000 + self.player.theme_id)#theme

        self.writeVInt(1)
        for x in range(1):
            self.writeVint(29)
            self.writeVint(5)
            self.writeVint(0)
            self.writeVint(3600)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeLong(self.player.ID)

        self.writeVInt(3)#Notification Array
        self.writeVInt(81) #нотиф айди
        self.writeInt(0)
        self.writeVInt(0)
        self.writeInt(0)
        self.writeString(f"Добро пожаловать!\nТвой токен: {self.player.name}")# текст
        self.writeVInt(1)
        
        self.writeVInt(83)
        self.writeInt(0)
        self.writeBoolean(True)
        self.writeInt(0)
        self.writeString()
        self.writeInt(0)
        self.writeString("Добро пожаловать в VL Brawl!")
        self.writeInt(0)
        self.writeString("А ты знал, что у нас есть свой Telegram канал?")

        self.writeInt(0)
        self.writeString("Telegram")

        self.writeString("/36042168-49af-4e79-b5f3-13c8c279bc5c_brawltalkpopup.png")
        self.writeString('28d8d5533ddecebf766daac49f3290415a36fa42')

        self.writeString("brawlstars://extlink?page=https%3A%2F%2Ft.me%2Fvlbruh")
        self.writeVInt(3473)
        
        self.writeVInt(64) 
        self.writeInt(2)
        self.writeBoolean(False)
        self.writeInt(0)
        self.writeString("")
        self.writeVInt(1)
        self.writeVInt(16)#Id
        self.writeVInt(1)
        
        #Notification Array End

        self.writeVInt(0)

        self.writeUInt8(0)

        self.writeVInt(0)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)