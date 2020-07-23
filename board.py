# board.py

import pygame
pygame.init()

squares = {} # square names matched to their cords
for i in range(1, 9):
    for j, file in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
        squares[file + str(i)] = (16 + 96*j, 800 - 16 - 96*i)


board = pygame.image.load("Images\Board.png") # board image

class Board(object):
    '''
    Board object containing most of the game
    '''

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.pieces = []
        self.turn = 'White'
        self.selected_piece = None
        self.occupied = {}


    def get_square(cords):
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


    def setup(self):
        # pawns
        for i in range(8):
            self.pieces.append(Pawn("White", chr(ord('a') + i) + '2'))
            self.occupied[chr(ord('a') + i) + '2'] = self.pieces[-1]

        for i in range(8):
            self.pieces.append(Pawn("Black", chr(ord('a') + i) + '7'))
            self.occupied[chr(ord('a') + i) + '7'] = self.pieces[-1]

        # bishops
        self.pieces.append(Bishop("White", 'c1'))
        self.occupied['c1'] = self.pieces[-1]
        self.pieces.append(Bishop("White", 'f1'))
        self.occupied['f1'] = self.pieces[-1]

        self.pieces.append(Bishop("Black", 'c8'))
        self.occupied['c8'] = self.pieces[-1]
        self.pieces.append(Bishop("Black", 'f8'))
        self.occupied['f8'] = self.pieces[-1]

        # knights
        self.pieces.append(Knight("White", 'b1'))
        self.occupied['b1'] = self.pieces[-1]
        self.pieces.append(Knight("White", 'g1'))
        self.occupied['g1'] = self.pieces[-1]

        self.pieces.append(Knight("Black", 'b8'))
        self.occupied['b8'] = self.pieces[-1]
        self.pieces.append(Knight("Black", 'g8'))
        self.occupied['g8'] = self.pieces[-1]

        # rooks
        self.pieces.append(Rook("White", 'a1'))
        self.occupied['a1'] = self.pieces[-1]
        self.pieces.append(Rook("White", 'h1'))
        self.occupied['h1'] = self.pieces[-1]

        self.pieces.append(Rook("Black", 'a8'))
        self.occupied['a8'] = self.pieces[-1]
        self.pieces.append(Rook("Black", 'h8'))
        self.occupied['h8'] = self.pieces[-1]

        # queens and kings
        self.pieces.append(Queen("White", 'd1'))
        self.occupied['d1'] = self.pieces[-1]
        self.pieces.append(Queen("Black", 'd8'))
        self.occupied['d8'] = self.pieces[-1]

        self.pieces.append(King("White", 'e1'))
        self.occupied['e1'] = self.pieces[-1]
        self.pieces.append(King("Black", 'e8'))
        self.occupied['e8'] = self.pieces[-1]


    def draw(self, canvas):
        # draw the board
        board = pygame.transform.scale(board, (self.size, self.size))
        canvas.blit(board, (self.x, self.y))


    def lift_piece(self, pos):
        sq = self.get_square(pos)
        if sq == None:
            return

        # pick up a piece when none are selected
        if self.occupied[sq] != None and self.selected_piece == None and self.occupied[sq].colour == self.turn:
            self.selected_piece = self.occupied[sq]
            selected_piece.state = 'Lifted'
            selected_piece.cords = (pos[0] - 48, pos[1] - 48)
        # select a different piece
        elif selected_piece != None and sq not in selected_piece.legal_moves(piece_list, occupied):
            selected_piece.state = 'Down'
            if occupied[sq] != None and occupied[sq].colour == turn:
                selected_piece = occupied[sq]
                selected_piece.state = 'Lifted'
                selected_piece.cords = (pos[0] - 48, pos[1] - 48)
            else:
                selected_piece = None
