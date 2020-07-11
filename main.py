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


def setup():
    '''
    Crop images of the pieces and initialize their positions

    pygame.draw.rect(screen, (0,0,0), (16,16,96,96))
    Tested the board image, the size of a square is exactly 96x96 and the board
    starts at (16, 16) when not including the border

    Returns a list of all piece objects
    '''
    piece_list = []

    # pawns
    for i in range(8):
        piece_list.append(Piece("Pawn", "White", chr(ord('a') + i) + '2'))
        # screen.blit(w_Pawn, (16+96*i, 16+96*6))

    for i in range(8):
        piece_list.append(Piece("Pawn", "Black", chr(ord('a') + i) + '7'))

    # bishops
    piece_list.append(Piece("Bishop", "White", 'c1'))
    piece_list.append(Piece("Bishop", "White", 'f1'))

    piece_list.append(Piece("Bishop", "Black", 'c8'))
    piece_list.append(Piece("Bishop", "Black", 'f8'))

    # knights
    piece_list.append(Piece("Knight", "White", 'b1'))
    piece_list.append(Piece("Knight", "White", 'g1'))

    piece_list.append(Piece("Knight", "Black", 'b8'))
    piece_list.append(Piece("Knight", "Black", 'g8'))

    # rooks
    piece_list.append(Piece("Rook", "White", 'a1'))
    piece_list.append(Piece("Rook", "White", 'h1'))

    piece_list.append(Piece("Rook", "Black", 'a8'))
    piece_list.append(Piece("Rook", "Black", 'h8'))

    # queens and kings
    piece_list.append(Piece("Queen", "White", 'd1'))
    piece_list.append(Piece("Queen", "Black", 'd8'))

    piece_list.append(Piece("King", "White", 'e1'))
    piece_list.append(Piece("King", "Black", 'e8'))

    return piece_list


def drawWindow(window, piece_list):
    global board, pieces

    # draw the board
    board = pygame.transform.scale(board, (WIDTH, HEIGHT))
    screen.blit(board, (0,0))

    # draw pieces
    for piece in piece_list:
        piece.draw(screen)

    pygame.display.update()


piece_list = setup()

inUse = True
while inUse:
    pygame.time.delay(50)
    drawWindow(screen, piece_list)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inUse = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inUse = False


pygame.quit()
