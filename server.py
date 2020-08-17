# server.py

import pygame
import socket
import pickle
from _thread import *
from board import Board
pygame.display.quit()

WIDTH = 800
HEIGHT = 800

server = '192.168.2.179'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

setup = Board(0, 0, HEIGHT, 'White')
setup.setup()
boards = ['White', 'Black']
occupied = setup.occupied.copy()
piece_list = setup.piece_list[:]


def threaded_client(conn, player):
    global piece_list, occupied
    conn.send(pickle.dumps(boards[player]))

    reply = ""
    while True:
        try:
            # data should be a tuple in the form (piece_list, occupied, function)
            data = pickle.loads(conn.recv(1024 * 8))

            if not data:
                break
            else:
                if data[2] == 'get':
                    reply = (piece_list, occupied)
                elif data[2] == 'update':
                    reply = data
                    piece_list = data[0]
                    occupied = data[1]

                # print("Received: ", data)
                # print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))

        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    if currentPlayer > 1:
        currentPlayer = 0
