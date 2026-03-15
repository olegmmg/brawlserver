from ByteStream.Reader import Reader
from Protocol.Messages.Server.Aliance.AllianceResponseMessage import AllianceResponseMessage
from Protocol.Messages.Server.Aliance.MyAllianceMessage import MyAllianceMessage
from Protocol.Messages.Server.Aliance.AllianceDataMessage import AllianceDataMessage


class ChangeAllianceSettingsMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        MyAllianceMessage(self.client, self.player, club_data).send()
        AllianceResponseMessage(self.client, self.player, 10).send()
        AllianceDataMessage(self.client, self.player, club_data).send()