# main.py

import pygame
from pieces import *
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame Chess')

# images
board = pygame.image.load("Board.png")
pieces = pygame.image.load("Pieces.png") # spritesheet of all pieces
circle = pygame.image.load("circle.png")
circle = pygame.transform.scale(circle, (96, 96)).convert_alpha()
circle.fill((255, 255, 255, 100), None, pygame.BLEND_RGBA_MULT)
# sounds
move = pygame.mixer.Sound("Move.wav")
capture = pygame.mixer.Sound("Capture.wav")



squares = {} # square names matched to their cords
occupied = {}
for i in range(1, 9):
    for j, file in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
        squares[file + str(i)] = (16 + 96*j, 800 - 16 - 96*i)
        # rows 1, 2, 7, and 8 are occupied at the beginning
        occupied[file + str(i)] = None


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
        piece_list.append(Pawn("White", chr(ord('a') + i) + '2'))
        occupied[chr(ord('a') + i) + '2'] = piece_list[-1]

    for i in range(8):
        piece_list.append(Pawn("Black", chr(ord('a') + i) + '7'))
        occupied[chr(ord('a') + i) + '7'] = piece_list[-1]

    # bishops
    piece_list.append(Bishop("White", 'c1'))
    occupied['c1'] = piece_list[-1]
    piece_list.append(Bishop("White", 'f1'))
    occupied['f1'] = piece_list[-1]

    piece_list.append(Bishop("Black", 'c8'))
    occupied['c8'] = piece_list[-1]
    piece_list.append(Bishop("Black", 'f8'))
    occupied['f8'] = piece_list[-1]

    # knights
    piece_list.append(Knight("White", 'b1'))
    occupied['b1'] = piece_list[-1]
    piece_list.append(Knight("White", 'g1'))
    occupied['g1'] = piece_list[-1]

    piece_list.append(Knight("Black", 'b8'))
    occupied['b8'] = piece_list[-1]
    piece_list.append(Knight("Black", 'g8'))
    occupied['g8'] = piece_list[-1]

    # rooks
    piece_list.append(Rook("White", 'a1'))
    occupied['a1'] = piece_list[-1]
    piece_list.append(Rook("White", 'h1'))
    occupied['h1'] = piece_list[-1]

    piece_list.append(Rook("Black", 'a8'))
    occupied['a8'] = piece_list[-1]
    piece_list.append(Rook("Black", 'h8'))
    occupied['h8'] = piece_list[-1]

    # queens and kings
    piece_list.append(Queen("White", 'd1'))
    occupied['d1'] = piece_list[-1]
    piece_list.append(Queen("Black", 'd8'))
    occupied['d8'] = piece_list[-1]

    piece_list.append(King("White", 'e1'))
    occupied['e1'] = piece_list[-1]
    piece_list.append(King("Black", 'e8'))
    occupied['e8'] = piece_list[-1]

    return piece_list


def get_square(cords):
    '''
    Returns the square that is at the given cords
    Note: cords on the border returns None
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


def drawWindow(window, piece_list):
    global board, pieces

    # draw the board
    board = pygame.transform.scale(board, (WIDTH, HEIGHT))
    screen.blit(board, (0,0))

    # draw pieces
    for piece in piece_list:
        piece.draw(screen, circle)

    pygame.display.update()


piece_list = setup()
selected_piece = None

inUse = True
while inUse:
    pygame.time.delay(10)
    drawWindow(screen, piece_list)

    if selected_piece != None:
        pos = pygame.mouse.get_pos()
        selected_piece.cords = (pos[0] - 48, pos[1] - 48)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inUse = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inUse = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                if occupied[get_square(pos)] != None and selected_piece == None: # select a piece
                    if selected_piece != None:
                        selected_piece.state = 'Down'
                    selected_piece = occupied[get_square(pos)]
                    selected_piece.state = 'Lifted'
                    selected_piece.cords = (pos[0] - 48, pos[1] - 48)
                    print("possible moves: ", selected_piece.legal_moves(piece_list, occupied))
                elif selected_piece != None and get_square(pos) == selected_piece.position:
                    selected_piece.state = 'Lifted'
                    selected_piece.cords = (pos[0] - 48, pos[1] - 48)
                    print("possible moves: ", selected_piece.legal_moves(piece_list, occupied))
                elif selected_piece != None and get_square(pos) in selected_piece.legal_moves(piece_list, occupied):
                    # use move function when made


        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            sq = get_square(pos)
            if selected_piece != None and sq != None:
                if sq == selected_piece.position: # check for click to move
                    selected_piece.state = 'Selected'
                elif sq in selected_piece.legal_moves(piece_list, occupied): # check for drag to move
                    move.play()
                    occupied[selected_piece.position] = None
                    occupied[sq] = selected_piece
                    selected_piece.position = sq
                    selected_piece.state = 'Down'
                    selected_piece = None
                elif selected_piece.state == 'Lifted':
                    selected_piece.state = 'Down'
            elif selected_piece != None:
                selected_piece.state = 'Down'
                selected_piece = None

pygame.quit()
