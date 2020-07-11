# pieces.py

import pygame
pygame.init()

pieces = pygame.image.load("Pieces.png") # spritesheet of all pieces

# square names matched to their cords
squares = {}
for i in range(1, 9):
    for j, file in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
        squares[file + str(i)] = (16 + 96*j, 800 - 16 - 96*i)


class Piece(object):

    def __init__(self, type, colour, position):
        self.type = type # 'Pawn' 'Bishop' 'Rook' 'Knight' 'Queen' 'King'
        self.colour = colour
        if colour == 'White':
            if type == 'Pawn':
                image = pieces.subsurface((1750, 10, 332, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'Bishop':
                image = pieces.subsurface((703, 0, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'Knight':
                image = pieces.subsurface((1050, 0, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'Rook':
                image = pieces.subsurface((1400, 0, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'Queen':
                image = pieces.subsurface((355, 0, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'King':
                image = pieces.subsurface((5, 0, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
        elif colour == 'Black':
            if type == 'Pawn':
                image = pieces.subsurface((1750, 350, 332, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'Bishop':
                image = pieces.subsurface((703, 350, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'Knight':
                image = pieces.subsurface((1050, 350, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'Rook':
                image = pieces.subsurface((1400, 350, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'Queen':
                image = pieces.subsurface((355, 350, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'King':
                image = pieces.subsurface((5, 350, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
        self.position = position


    def draw(self, screen):
        screen.blit(self.image, squares[self.position])


    def move(self):
        pass
