# Protocol/Messages/Server/TutorialProgressMessage.py
from ByteStream.Writer import Writer

class TutorialProgressMessage(Writer):
    def __init__(self, client, player, tutorial_state):
        super().__init__(client)
        self.id = 20199  # ID может быть другим, проверьте правильный ID
        self.player = player
        self.tutorial_state = tutorial_state

    def encode(self):
        self.writeVInt(self.tutorial_state)
        print(f"[TutorialProgress] Sent tutorial state: {self.tutorial_state}")