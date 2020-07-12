# pieces.py

import pygame
pygame.init()

pieces = pygame.image.load("Pieces.png") # spritesheet of all pieces

# square names matched to their cords
squares = {}
for i in range(1, 9):
    for j, file in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
        squares[file + str(i)] = (16 + 96*j, 800 - 16 - 96*i)


class Piece(object):

    def __init__(self, type, colour, position):
        self.type = type # 'Pawn' 'Bishop' 'Rook' 'Knight' 'Queen' 'King'
        self.colour = colour
        if colour == 'White':
            if type == 'Pawn':
                image = pieces.subsurface((1750, 10, 332, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'Bishop':
                image = pieces.subsurface((703, 0, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'Knight':
                image = pieces.subsurface((1050, 0, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'Rook':
                image = pieces.subsurface((1400, 0, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'Queen':
                image = pieces.subsurface((355, 0, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'King':
                image = pieces.subsurface((5, 0, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
        elif colour == 'Black':
            if type == 'Pawn':
                image = pieces.subsurface((1750, 350, 332, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'Bishop':
                image = pieces.subsurface((703, 350, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'Knight':
                image = pieces.subsurface((1050, 350, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'Rook':
                image = pieces.subsurface((1400, 350, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'Queen':
                image = pieces.subsurface((355, 350, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
            elif type == 'King':
                image = pieces.subsurface((5, 350, 340, 340))
                image = pygame.transform.scale(image, (96, 96)).convert_alpha()
                self.image = image
        self.position = position
        self.state = 'Down' # 'Down' 'Lifted' or 'Selected'
        self.cords = (0, 0)


    def draw(self, screen):
        if self.state == 'Down':
            screen.blit(self.image, squares[self.position])
        else:
            screen.blit(self.image, self.cords)


    def legal_moves(self, piece_list, occupied):
        '''
        Returns a list of squares a piece can move to
        '''
        legal = []
        if self.type == 'Pawn':
            if self.colour == 'White':
                if occupied[self.position[0] + str(int(self.position[1]) + 1)] == None:
                    legal.append(self.position[0] + str(int(self.position[1]) + 1))
                    # check if pawn is on starting square, if so it can move 2 squares forward
                    if self.position[1] == '2' and occupied[self.position[0] + str(int(self.position[1]) + 2)] == None:
                        legal.append(self.position[0] + str(int(self.position[1]) + 2))

                # check squares diagonal and infront to see if you can move by capturing
                dia1 = chr(ord(self.position[0]) - 1) + str(int(self.position[1]) + 1)
                dia2 = chr(ord(self.position[0]) + 1) + str(int(self.position[1]) + 1)
                if self.position[0] != 'a' and occupied[dia1] != None and occupied[dia1].colour != self.colour:
                    legal.append(dia1)
                if self.position[0] != 'h' and occupied[dia2] != None and occupied[dia2].colour != self.colour:
                    legal.append(dia2)

            elif self.colour == 'Black':
                if occupied[self.position[0] + str(int(self.position[1]) - 1)] == None:
                    legal.append(self.position[0] + str(int(self.position[1]) - 1))
                    # check if pawn is on starting square, if so it can move 2 squares forward
                    if self.position[1] == '7' and occupied[self.position[0] + str(int(self.position[1]) - 2)] == None:
                        legal.append(self.position[0] + str(int(self.position[1]) - 2))

                # check squares diagonal and infront to see if you can move by capturing
                dia1 = chr(ord(self.position[0]) - 1) + str(int(self.position[1]) - 1)
                dia2 = chr(ord(self.position[0]) + 1) + str(int(self.position[1]) - 1)
                if self.position[0] != 'a' and occupied[dia1] != None and occupied[dia1].colour != self.colour:
                    legal.append(dia1)
                if self.position[0] != 'h' and occupied[dia2] != None and occupied[dia2].colour != self.colour:
                    legal.append(dia2)

        elif self.type == 'Bishop':
            diagonal = 1
            paths = [True, True, True, True] # top left, top right, bottom right, bottom left
            # checks all diagonals that are 'diagonal' units away from the position
            if self.position[0] == 'a':
                paths[0] = False
                paths[3] = False
            elif self.position[0] == 'h':
                paths[1] = False
                paths[2] = False

            if self.position[1] == '1':
                paths[2] = False
                paths[3] = False
            elif self.position[1] == '8':
                paths[0] = False
                paths[1] = False

            while True in paths:
                if paths[0]:
                    sq = chr(ord(self.position[0]) - diagonal) + str(int(self.position[1]) + diagonal)
                    if sq[0] == 'a' or sq[1] == '8':
                        paths[0] = False
                        if occupied[sq] == None:
                            legal.append(sq)
                    elif occupied[sq] == None:
                        legal.append(sq)
                    else:
                        paths[0] = False
                if paths[1]:
                    sq = chr(ord(self.position[0]) + diagonal) + str(int(self.position[1]) + diagonal)
                    if sq[0] == 'h' or sq[1] == '8':
                        paths[1] = False
                        if occupied[sq] == None:
                            legal.append(sq)
                    elif occupied[sq] == None:
                        legal.append(sq)
                    else:
                        paths[1] = False
                if paths[2]:
                    sq = chr(ord(self.position[0]) + diagonal) + str(int(self.position[1]) - diagonal)
                    if sq[0] == 'h' or sq[1] == '1':
                        paths[2] = False
                        if occupied[sq] == None:
                            legal.append(sq)
                    elif occupied[sq] == None:
                        legal.append(sq)
                    else:
                        paths[2] = False
                if paths[3]:
                    sq = chr(ord(self.position[0]) - diagonal) + str(int(self.position[1]) - diagonal)
                    if sq[0] == 'a' or sq[1] == '1':
                        paths[3] = False
                        if occupied[sq] == None:
                            legal.append(sq)
                    elif occupied[sq] == None:
                        legal.append(sq)
                    else:
                        paths[3] = False

                diagonal += 1

        elif self.type == 'Knight':
            pass

        elif self.type == 'Rook':
            pass

        elif self.type == 'Queen':
            pass

        elif self.type == 'King':
            pass

        return legal
