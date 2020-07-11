# main.py

import pygame
from pieces import Piece
pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# images
board = pygame.image.load("Board.png")
pieces = pygame.image.load("Pieces.png") # spritesheet of all pieces

# square names matched to their cords
squares = {}
for i in range(1, 9):
    for j, file in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
        squares[file + str(i)] = (16 + 96*j, 16 + 96*i)


def setup():
    '''
    Crop images of the pieces and initialize their cords
    '''
    pieces = {}


def drawWindow(window):
    global board, pieces
    # draw the board
    board = pygame.transform.scale(board, (WIDTH, HEIGHT))
    screen.blit(board, (0,0))

    # crop and draw pieces
    '''
    pygame.draw.rect(screen, (0,0,0), (16,16,96,96))
    Tested the image, the size of a square is exactly 96x96 and the board starts
    at (16, 16) when not including the border
    '''

    # pawns
    w_Pawns = []
    for i in range(8):
        w_Pawn = pieces.subsurface((1750, 10, 332, 340))
        w_Pawn = pygame.transform.scale(w_Pawn, (96, 96)).convert()
        screen.blit(w_Pawn, (16+96*i, 16+96*6))

    pygame.display.update()


inUse = True
while inUse:
    pygame.time.delay(50)
    drawWindow(screen)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inUse = False


pygame.quit()
