# board.py

import pygame
from pieces import *
from button import *
pygame.init()

squares = {} # square names matched to their cords
for i in range(1, 9):
    for j, file in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
        squares[file + str(i)] = (16 + 96*j, 800 - 16 - 96*i)


circle = pygame.image.load("Images\circle.png")
circle = pygame.transform.scale(circle, (96, 96)).convert_alpha()
circle.fill((255, 255, 255, 100), None, pygame.BLEND_RGBA_MULT)


class Board(object):
    '''
    Board object containing most of the game
    '''

    def __init__(self, x, y, size, player):
        self.x = x
        self.y = y
        self.size = size
        self.player = player
        self.piece_list = []
        self.turn = 'White'
        self.selected_piece = None
        self.occupied = {}
        for i in range(1, 9):
            for j, file in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
                self.occupied[file + str(i)] = None
        self.game_over = False
        self.winner = None
        self.image = pygame.transform.scale(pygame.image.load("Images\Board.png"), (self.size, self.size))

    @staticmethod
    def get_square(cords, player):
        '''
        Returns the square that is at the given cords
        Note: cords on the border returns None
        NOTE: This func only works for an 800x800 board
        Reminder to change this later:
            2% of the boards width and height are made by the border,
            so that can be used to make each square about 12% of the width and
            height of the board size
        '''
        for cord in cords:
            if cord >= 784 or cord <= 16:
                return None

        col = None
        for j, file in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
            if player == 'White':
                if 16 + 96*j > cords[0]:
                    col = chr(ord(file) - 1)
                    break
            else: # if player == 'Black'
                if 800 - 16 - 96*j < cords[0]:
                    col = chr(ord(file) - 1)
                    break
        if col == None:
            col = 'h'

        row = None
        for i in range(1, 9):
            if player == 'White':
                if 800 - 16 - 96*i < cords[1]:
                    row = str(i)
                    break
            else:  # if player == 'Black'
                if 16 + 96*(i-1) > cords[1]:
                    row = str(i - 1)
                    break
        if row is None:
            row = '8'

        return col + row

    def is_checkmate(self):
        '''
        Returns if colour is checkmated
        Returns 'stalemate' if stalemate
        '''
        for piece in self.piece_list:
            if piece.colour == self.turn and piece.legal_moves(self.piece_list, self.occupied) != []:
                return False
            if str(type(piece)) == "<class 'pieces.King'>" and piece.colour == self.turn:
                king = piece
        if king.in_check(self.piece_list, self.occupied):
            return True
        else:
            return 'stalemate'

    def setup(self):
        self.selected_piece = None
        self.turn = 'White'
        self.game_over = False
        self.winner = None
        self.piece_list = []
        for i in range(1, 9):
            for j, file in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
                self.occupied[file + str(i)] = None
        # pawns
        for i in range(8):
            self.piece_list.append(Pawn("White", chr(ord('a') + i) + '2'))
            self.occupied[chr(ord('a') + i) + '2'] = self.piece_list[-1]

        for i in range(8):
            self.piece_list.append(Pawn("Black", chr(ord('a') + i) + '7'))
            self.occupied[chr(ord('a') + i) + '7'] = self.piece_list[-1]

        # bishops
        self.piece_list.append(Bishop("White", 'c1'))
        self.occupied['c1'] = self.piece_list[-1]
        self.piece_list.append(Bishop("White", 'f1'))
        self.occupied['f1'] = self.piece_list[-1]

        self.piece_list.append(Bishop("Black", 'c8'))
        self.occupied['c8'] = self.piece_list[-1]
        self.piece_list.append(Bishop("Black", 'f8'))
        self.occupied['f8'] = self.piece_list[-1]

        # knights
        self.piece_list.append(Knight("White", 'b1'))
        self.occupied['b1'] = self.piece_list[-1]
        self.piece_list.append(Knight("White", 'g1'))
        self.occupied['g1'] = self.piece_list[-1]

        self.piece_list.append(Knight("Black", 'b8'))
        self.occupied['b8'] = self.piece_list[-1]
        self.piece_list.append(Knight("Black", 'g8'))
        self.occupied['g8'] = self.piece_list[-1]

        # rooks
        self.piece_list.append(Rook("White", 'a1'))
        self.occupied['a1'] = self.piece_list[-1]
        self.piece_list.append(Rook("White", 'h1'))
        self.occupied['h1'] = self.piece_list[-1]

        self.piece_list.append(Rook("Black", 'a8'))
        self.occupied['a8'] = self.piece_list[-1]
        self.piece_list.append(Rook("Black", 'h8'))
        self.occupied['h8'] = self.piece_list[-1]

        # queens and kings
        self.piece_list.append(Queen("White", 'd1'))
        self.occupied['d1'] = self.piece_list[-1]
        self.piece_list.append(Queen("Black", 'd8'))
        self.occupied['d8'] = self.piece_list[-1]

        self.piece_list.append(King("White", 'e1'))
        self.occupied['e1'] = self.piece_list[-1]
        self.piece_list.append(King("Black", 'e8'))
        self.occupied['e8'] = self.piece_list[-1]

    def draw(self, canvas, font):
        # draw the board
        canvas.blit(self.image, (self.x, self.y))

        if self.selected_piece is not None:
            pos = pygame.mouse.get_pos()
            self.selected_piece.cords = (pos[0] - 48, pos[1] - 48)

        # draw pieces
        lifted = None
        for piece in self.piece_list:
            if piece != self.selected_piece:
                piece.draw(canvas, circle, self.piece_list, self.occupied, self.player)
            else:
                lifted = piece
        if lifted is not None: # draw lifted piece last so that it is at the front
            lifted.draw(canvas, circle, self.piece_list, self.occupied, self.player)

    def lift_piece(self, pos):
        if self.game_over:
            return

        sq = self.get_square(pos, self.player)
        if sq is None:
            return

        # pick up a piece when none are selected
        if self.occupied[sq] is not None and self.selected_piece is None and self.occupied[sq].colour == self.turn:
            self.selected_piece = self.occupied[sq]
            self.selected_piece.state = 'Lifted'
            self.selected_piece.cords = (pos[0] - 48, pos[1] - 48)
        # select a different piece
        elif self.selected_piece is not None and sq not in self.selected_piece.legal_moves(self.piece_list, self.occupied):
            self.selected_piece.state = 'Down'
            if self.occupied[sq] is not None and self.occupied[sq].colour == self.turn:
                self.selected_piece = self.occupied[sq]
                self.selected_piece.state = 'Lifted'
                self.selected_piece.cords = (pos[0] - 48, pos[1] - 48)
            else:
                self.selected_piece = None

    def move_piece(self, pos):
        if self.game_over:
            return

        sq = self.get_square(pos, self.player)
        if self.selected_piece is not None and sq is not None:  # check if a piece is selected
            if sq == self.selected_piece.position:  # check for click to move
                self.selected_piece.state = 'Selected'
            # check for drag to move
            elif sq in self.selected_piece.legal_moves(self.piece_list, self.occupied):
                self.reset_enpassant()
                self.selected_piece.move(sq, self.piece_list, self.occupied)
                # check for pawn promotion
                if str(type(self.selected_piece)) == "<class 'pieces.Pawn'>":
                    self.selected_piece.promote(self.piece_list, self.occupied)

                self.selected_piece = None

                # swap turns
                if self.turn == 'White':
                    self.turn = 'Black'
                else:
                    self.turn = 'White'

                # check for checkmate after each move
                mate = self.is_checkmate()
                if mate is True:
                    if self.turn == 'White':
                        self.winner = 'Black'
                    else:
                        self.winner = 'White'
                    self.game_over = True
                elif mate == 'stalemate':
                    self.winner = 'stalemate'
                    self.game_over = True

            # unselected if illegal move
            elif self.selected_piece.state == 'Lifted':
                self.selected_piece.state = 'Down'
        elif self.selected_piece is not None:
            self.selected_piece.state = 'Down'
            self.selected_piece = None

    def reset_enpassant(self):
        '''
        Small func to set the ability to en passant to false after a turn in which it is true
        '''
        for piece in self.piece_list:
            if str(type(piece)) == "<class 'pieces.Pawn'>" and piece.en_passant:
                piece.en_passant = False
