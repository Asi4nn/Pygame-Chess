# chess.py

import pygame

pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)  # for some reason you have to init the mixer twice to not have sound delay

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame Chess')

# you have to set the display mode before transforming images inside the
# classes for some reason
from button import Button
from board import Board
from network import Network

calibri = pygame.font.SysFont('calibri', 100)

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
    n = Network()
    colour = n.getBoard()
    board = Board(0, 0, HEIGHT, colour)
    board.setup()

    while True:
        pygame.time.delay(10)
        board.update(n.send((board.piece_list, board.occupied, 'get')))
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
                    board.update(n.send((board.piece_list, board.occupied, 'update')))
                else:
                    if play_again.isPressed(pos):
                        board.setup()


game_loop(screen)  # run the game
pygame.quit()
