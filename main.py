# main.py

import pygame
from pieces import *
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024) # for some reason you have to init the mixer twice to not have sound delay

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


def is_checkmate(piece_list, colour):
    '''
    Returns if colour is checkmated
    Returns 'stalemate' if stalemate
    '''
    for piece in piece_list:
        if piece.colour == colour and piece.legal_moves(piece_list, occupied) != []:
            return False
        if str(type(piece)) == "<class 'pieces.King'>" and piece.colour == colour:
            king = piece
    if king.in_check(piece_list, occupied):
        return True
    else:
        return 'stalemate'


def printText(text, font, canvas, x, y):
    theText = font.render(text, 1, (0,0,0))
    textbox = theText.get_rect()
    textbox.center = (x, y)
    canvas.blit(theText, textbox)


def drawWindow(screen, piece_list):
    global board, pieces

    # draw the board
    board = pygame.transform.scale(board, (800, 800))
    screen.blit(board, (0,0))


    # draw pieces
    lifted = None
    for piece in piece_list:
        if piece != selected_piece:
            piece.draw(screen, circle, piece_list, occupied)
        else:
            lifted = piece
    if lifted != None: # draw lifted piece last so that it is at the front
        lifted.draw(screen, circle, piece_list, occupied)

    pygame.display.update()


piece_list = setup()
selected_piece = None
turn = 'White'
game_over = False

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
            sq = get_square(pos)
            if pygame.mouse.get_pressed()[0]:
                if sq != None and occupied[sq] != None and selected_piece == None and occupied[sq].colour == turn: # pick up a piece when none are selected
                    selected_piece = occupied[sq]
                    selected_piece.state = 'Lifted'
                    selected_piece.cords = (pos[0] - 48, pos[1] - 48)
                    # print("possible moves: ", selected_piece.legal_moves(piece_list, occupied))
                elif sq != None and selected_piece != None and sq not in selected_piece.legal_moves(piece_list, occupied): # select a different piece
                    selected_piece.state = 'Down'
                    if occupied[sq] != None and occupied[sq].colour == turn:
                        selected_piece = occupied[sq]
                        selected_piece.state = 'Lifted'
                        selected_piece.cords = (pos[0] - 48, pos[1] - 48)
                    else:
                        selected_piece = None


        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            sq = get_square(pos)
            if selected_piece != None and sq != None: # check if a piece is selected
                if sq == selected_piece.position: # check for click to move
                    selected_piece.state = 'Selected'
                elif sq in selected_piece.legal_moves(piece_list, occupied): # check for drag to move
                    selected_piece.move(sq, piece_list, occupied)
                    # check for pawn promotion
                    if str(type(selected_piece)) == "<class 'pieces.Pawn'>":
                        selected_piece.promote(piece_list, occupied)

                    selected_piece = None
                    if turn == 'White':
                        turn = 'Black'
                    else:
                        turn = 'White'
                    if is_checkmate(piece_list, turn) == True:
                        if turn == 'White':
                            print("Black wins")
                        else:
                            print("White wins")
                        inUse = False
                    elif is_checkmate(piece_list, turn) == 'stalemate':
                        print("Stalemate, no possible moves")
                        inUse = False
                elif selected_piece.state == 'Lifted': # unselected if illegal move
                    selected_piece.state = 'Down'
            elif selected_piece != None:
                selected_piece.state = 'Down'
                selected_piece = None

pygame.quit()
