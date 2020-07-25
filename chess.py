# chess.py

import pygame
from pieces import *
from button import *
from board import *
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024) # for some reason you have to init the mixer twice to not have sound delay

WIDTH = 800
HEIGHT = 800

calibri = pygame.font.SysFont('calibri', 100)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame Chess')

# images
circle = pygame.image.load("Images\circle.png")
circle = pygame.transform.scale(circle, (96, 96)).convert_alpha()
circle.fill((255, 255, 255, 100), None, pygame.BLEND_RGBA_MULT)

# buttons
play_again = Button(250, 500, 300, 100, 'Play Again', (127, 127, 127),
                    font_size=60)

def printText(text, font, canvas, x, y, colour):
    theText = font.render(text, 1, colour)
    textbox = theText.get_rect()
    textbox.center = (x, y)
    canvas.blit(theText, textbox)


def drawWindow(canvas, board):
    board.draw(screen, calibri)

    if board.game_over:
        if board.winner != 'stalemate':
            printText(board.winner + " wins", calibri, canvas, 400, 400, (255, 0, 0))
        else:
            printText('Stalemate', calibri, canvas, 400, 400, (255, 0, 0))
        play_again.draw(canvas)

    pygame.display.update()


def game_loop(screen):
    board = Board(0, 0, HEIGHT)
    board.setup()
    while True:
        pygame.time.delay(10)
        drawWindow(screen, board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if not board.game_over:
                    board.lift_piece(pos)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                if not board.game_over:
                    board.move_piece(pos)
                else:
                    print(play_again.isPressed(pos))
                    if play_again.isPressed(pos):
                        board.setup()


    '''
    while True:
        pygame.time.delay(10)
        drawWindow(screen, piece_list)

        if selected_piece != None:
            pos = pygame.mouse.get_pos()
            selected_piece.cords = (pos[0] - 48, pos[1] - 48)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                sq = get_square(pos)
                if pygame.mouse.get_pressed()[0]:
                    board.lift_piece(pos)
                    # pick up a piece when none are selected
                    if sq != None and occupied[sq] != None and selected_piece == None and occupied[sq].colour == turn:
                        selected_piece = occupied[sq]
                        selected_piece.state = 'Lifted'
                        selected_piece.cords = (pos[0] - 48, pos[1] - 48)
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
                    # check for drag to move
                    elif sq in selected_piece.legal_moves(piece_list, occupied):
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
                                winner = 'Black'
                            else:
                                winner = 'White'
                        elif is_checkmate(piece_list, turn) == 'stalemate':
                            winner = 'stalemate'
                    # unselected if illegal move
                    elif selected_piece.state == 'Lifted':
                        selected_piece.state = 'Down'
                elif selected_piece != None:
                    selected_piece.state = 'Down'
                    selected_piece = None
                    '''


'''
piece_list = setup()
selected_piece = None
turn = 'White'
game_over = False
winner = None
'''

game_loop(screen) # run the game
pygame.quit()
