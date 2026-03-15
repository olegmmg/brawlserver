import time
import json
import socket
from threading import Thread
from Logic.Player import Player
from Logic.Device import Device
from Utils.Helpers import Helpers
from Protocol.LogicLaserMessageFactory import packets

# Заглушка для необработанных пакетов
class UnhandledMessage:
    def __init__(self, client, player, initial_bytes):
        self.client = client
        self.player = player
        self.initial_bytes = initial_bytes
        
    def decode(self):
        pass
        
    def process(self):
        print(f"[Unhandled] Packet processed but not implemented")
        # Отправляем пустой ответ чтобы клиент не отключался
        try:
            self.client.send(b'\x00' * 7)
        except:
            pass

def _(*args):
    for arg in args:
        print(arg, end=' ')
    print()

class ClientThread(Thread):
    def __init__(self, client, address, db):
        super().__init__()
        self.client = client
        self.address = address
        self.db = db
        self.config = json.loads(open('config.json', 'r').read())
        self.device = Device(self.client)
        self.player = Player(self.device, self.db)
        self.last_packet_time = time.time()
        self.running = True

    def recvall(self, length: int):
        data = b''
        while len(data) < length and self.running:
            try:
                s = self.client.recv(length - len(data))
                if not s:
                    break
                data += s
            except:
                break
        return data

    def run(self):
        try:
            # Устанавливаем таймаут на сокет
            self.client.settimeout(5.0)
            
            # Отправляем начальное сообщение лобби
            from Protocol.Messages.Server.LobbyInfoMessage import LobbyInfoMessage
            LobbyInfoMessage(self.client, self.player).send()
            
            while self.running:
                try:
                    header = self.client.recv(7)
                    if not header:
                        break
                        
                    if len(header) == 7:
                        self.last_packet_time = time.time()
                        packet_id = int.from_bytes(header[:2], 'big')
                        packet_length = int.from_bytes(header[2:5], 'big')
                        packet_data = self.recvall(packet_length)
                        
                        if len(packet_data) == packet_length:
                            if packet_id in packets:
                                packet_name = packets[packet_id].__name__
                                _(f'[*] PacketID: {packet_id}, Name: {packet_name} Length: {packet_length}')
                                
                                try:
                                    message = packets[packet_id](self.client, self.player, packet_data)
                                    if hasattr(message, 'decode'):
                                        message.decode()
                                    if hasattr(message, 'process'):
                                        message.process()
                                    if packet_id == 10101:
                                        Helpers.connected_clients["Clients"][str(self.player.ID)] = {"SocketInfo": self.client}
                                except Exception as e:
                                    _(f'[!] Error processing packet {packet_id}: {e}')
                                    # При ошибке используем заглушку
                                    message = UnhandledMessage(self.client, self.player, packet_data)
                                    message.process()
                            else:
                                _(f'[*] Unhandled Packet! ID: {packet_id}, Length: {packet_length}')
                                # Используем общую заглушку для неизвестных пакетов
                                message = UnhandledMessage(self.client, self.player, packet_data)
                                message.process()
                    
                    # Проверяем таймаут (увеличено до 30 секунд)
                    if time.time() - self.last_packet_time > 30:
                        _(f"[*] Client timeout! IP: {self.address[0]}")
                        break
                        
                except socket.timeout:
                    # Таймаут чтения - нормальная ситуация, продолжаем цикл
                    continue
                except Exception as e:
                    _(f"[*] Error in packet processing: {e}")
                    break

        except Exception as e:
            _(f"[*] Client error: {e}")
        finally:
            self.running = False
            try:
                self.client.close()
            except:
                pass
            if hasattr(Helpers, 'connected_clients'):
                if 'ClientsCount' in Helpers.connected_clients:
                    Helpers.connected_clients['ClientsCount'] -= 1
                if 'Clients' in Helpers.connected_clients and str(self.player.ID) in Helpers.connected_clients['Clients']:
                    del Helpers.connected_clients['Clients'][str(self.player.ID)]
            _(f"[*] Client disconnected! IP: {self.address[0]}")