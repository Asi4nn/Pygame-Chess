# pieces.py

import pygame

class Piece(object):

    def __init__(self, type, colour, image, cords):
        self.type = type # 'Pawn' 'Bishop' 'Rook' 'Knight' 'Queen' 'King'
        self.colour = colour
        self.image = image
        self.cords = cords
