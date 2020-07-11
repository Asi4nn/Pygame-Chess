# pieces.py

import pygame

class Piece(object):

    def __init__(self, type, colour, image, position):
        self.type = type # 'Pawn' 'Bishop' 'Rook' 'Knight' 'Queen' 'King'
        self.colour = colour
        self.image = image
        self.position = position


    def draw(self):
        pass
