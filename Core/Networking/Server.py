import json
import socket
from Utils.Helpers import Helpers
from Core.Networking.ClientThread import ClientThread
from Protocol.Messages.Server.LoginFailedMessage import LoginFailedMessage
from Core.Matchmaking import MatchmakingManager

def _(*args):
    for arg in args:
        print(arg, end=' ')
    print()

class Server:
    clients_count = 0

    def __init__(self, ip: str, port: int):
        self.config = json.loads(open('config.json', 'r').read())
        self.server = socket.socket()
        self.port = port
        self.ip = ip

    def start(self):
        self.server.bind((self.ip, self.port))

        # Start matchmaking background loop
        MatchmakingManager.start_loop()
        _(f'{Helpers.green}[*] Matchmaking loop started!')
        _(f'{Helpers.green}[*] Server started! Listening on {self.ip}:{self.port}')

        while True:
            self.server.listen()
            client, address = self.server.accept()

            _(f'{Helpers.green}[*] Client connected! IP: {address[0]}')

            ClientThread(client, address).start()

            Helpers.connected_clients['ClientsCount'] += 1

        while True:
            self.server.listen()
            client, address = self.server.accept()

            _(f'{Helpers.green}[*] Client connected! IP: {address[0]}')

            ClientThread(client, address).start()

            Helpers.connected_clients['ClientsCount'] += 1