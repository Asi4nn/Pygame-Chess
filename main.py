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
        image = pieces.subsurface((1750, 10, 332, 340))
        image = pygame.transform.scale(image, (96, 96)).convert_alpha()
        piece_list.append(Piece("Pawn", "White", image, chr(ord('a') + i) + '2'))
        # screen.blit(w_Pawn, (16+96*i, 16+96*6))

    for i in range(8):
        image = pieces.subsurface((1750, 350, 332, 340))
        image = pygame.transform.scale(image, (96, 96)).convert_alpha()
        piece_list.append(Piece("Pawn", "Black", image, chr(ord('a') + i) + '7'))

    # bishops
    image = pieces.subsurface((703, 0, 340, 340))
    image = pygame.transform.scale(image, (96, 96)).convert_alpha()
    piece_list.append(Piece("Bishop", "White", image, 'c1'))

    image = pieces.subsurface((703, 0, 340, 340))
    image = pygame.transform.scale(image, (96, 96)).convert_alpha()
    piece_list.append(Piece("Bishop", "White", image, 'f1'))

    image = pieces.subsurface((703, 350, 340, 340))
    image = pygame.transform.scale(image, (96, 96)).convert_alpha()
    piece_list.append(Piece("Bishop", "Black", image, 'c8'))

    image = pieces.subsurface((703, 350, 340, 340))
    image = pygame.transform.scale(image, (96, 96)).convert_alpha()
    piece_list.append(Piece("Bishop", "Black", image, 'f8'))

    # knights
    image = pieces.subsurface((1050, 0, 340, 340))
    image = pygame.transform.scale(image, (96, 96)).convert_alpha()
    piece_list.append(Piece("Knight", "White", image, 'b1'))

    image = pieces.subsurface((1050, 0, 340, 340))
    image = pygame.transform.scale(image, (96, 96)).convert_alpha()
    piece_list.append(Piece("Knight", "White", image, 'g1'))

    image = pieces.subsurface((1050, 350, 340, 340))
    image = pygame.transform.scale(image, (96, 96)).convert_alpha()
    piece_list.append(Piece("Knight", "Black", image, 'b8'))

    image = pieces.subsurface((1050, 350, 340, 340))
    image = pygame.transform.scale(image, (96, 96)).convert_alpha()
    piece_list.append(Piece("Knight", "Black", image, 'g8'))

    # rooks
    image = pieces.subsurface((1398, 0, 340, 340))
    image = pygame.transform.scale(image, (96, 96)).convert_alpha()
    piece_list.append(Piece("Rook", "White", image, 'a1'))

    image = pieces.subsurface((1398, 0, 340, 340))
    image = pygame.transform.scale(image, (96, 96)).convert_alpha()
    piece_list.append(Piece("Rook", "White", image, 'h1'))

    image = pieces.subsurface((1398, 350, 340, 340))
    image = pygame.transform.scale(image, (96, 96)).convert_alpha()
    piece_list.append(Piece("Rook", "Black", image, 'a8'))

    image = pieces.subsurface((1398, 350, 340, 340))
    image = pygame.transform.scale(image, (96, 96)).convert_alpha()
    piece_list.append(Piece("Rook", "Black", image, 'h8'))

    # queens and kings
    image = pieces.subsurface((355, 0, 340, 340))
    image = pygame.transform.scale(image, (96, 96)).convert_alpha()
    piece_list.append(Piece("Queen", "White", image, 'd1'))

    image = pieces.subsurface((355, 350, 340, 340))
    image = pygame.transform.scale(image, (96, 96)).convert_alpha()
    piece_list.append(Piece("Queen", "Black", image, 'd8'))

    image = pieces.subsurface((5, 0, 340, 340))
    image = pygame.transform.scale(image, (96, 96)).convert_alpha()
    piece_list.append(Piece("King", "Black", image, 'e1'))

    image = pieces.subsurface((5, 350, 340, 340))
    image = pygame.transform.scale(image, (96, 96)).convert_alpha()
    piece_list.append(Piece("King", "Black", image, 'e8'))

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
