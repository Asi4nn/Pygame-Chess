# network.py

import socket

class Network:
    '''
    Network class to send info from client to client
    '''
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.2.179'
        self.port = 5555
        self.addr = (self.server, self.port)
        self.board = self.connect()


    def getBoard(self):
        return self.board


    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(1024 * 8).decode()
        except:
            pass


    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(1024 * 8).decode()
        except socket.error as e:
            print(e)
