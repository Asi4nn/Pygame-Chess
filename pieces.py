# pieces.py

import pygame
pygame.init()

# square names matched to their cords
squares = {}
for i in range(1, 9):
    for j, file in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
        squares[file + str(i)] = (16 + 96*j, 800 - 16 - 96*i)

class Piece(object):

    def __init__(self, type, colour, image, position):
        self.type = type # 'Pawn' 'Bishop' 'Rook' 'Knight' 'Queen' 'King'
        self.colour = colour
        self.image = image
        self.position = position


    def draw(self, screen):
        screen.blit(self.image, squares[self.position])


    def move(self):
        pass
