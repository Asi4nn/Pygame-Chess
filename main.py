# main.py

import pygame
from pieces import Piece
pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame Chess')

# images
board = pygame.image.load("Board.png")
pieces = pygame.image.load("Pieces.png") # spritesheet of all pieces

# square names matched to their cords
squares = {}
for i in range(1, 9):
    for j, file in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
        squares[file + str(i)] = (16 + 96*j, 800 - 16 - 96*i)


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


def get_square(cords):
    '''
    Returns the square that is at the given cords
    Note: clicking on the border returns None
    '''
    for cord in cords:
        if cord >= 784 or cord <= 16:
            return None

    col = None
    for j, file in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
        if 16 + 96*j > cords[0]:
            col = chr(ord(file) - 1)
            break
    if col == None:
        col = 'h'


    for i in range(1, 9):
        if 800 - 16 - 96*i < cords[1]:
            row = str(i)
            break

    return col + row


piece_list = setup()
lifted_piece = None

inUse = True
while inUse:
    pygame.time.delay(10)
    drawWindow(screen, piece_list)

    if lifted_piece != None:
        pos = pygame.mouse.get_pos()
        lifted_piece.cords = (pos[0] - 48, pos[1] - 48)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inUse = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inUse = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                for piece in piece_list:
                    if piece.position == get_square(pos):
                        piece.state = 'Lifted'
                        lifted_piece = piece
                        lifted_piece.cords = (pos[0] - 48, pos[1] - 48)
        elif event.type == pygame.MOUSEBUTTONUP:
            if lifted_piece != None:
                lifted_piece.state = 'Down'
                lifted_piece = None


pygame.quit()
