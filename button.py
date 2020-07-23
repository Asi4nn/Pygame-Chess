# button.py

import pygame
pygame.init()

class Button(object):
    '''
    Button object class
    '''

    def __init__(self, height, width, x, y, text, colour,
                 text_colour=(0, 0, 0), outline=0,
                 font='calibri', font_size=12):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.text = text
        self.colour = colour
        self.text_colour = text_colour
        self.outline = outline
        self.font = font
        self.font_size = font_size


    def draw(self, canvas):
        pygame.draw.rect(canvas, self.colour, (self.x,
                            self.y, self.height, self.width), self.outline)
        text = pygame.font.SysFont(self.font, self.font_size).render(self.text, 1, self.text_colour)
        textbox = text.get_rect()
        textbox.center = (self.x + self.height//2, self.y + self.width//2)
        canvas.blit(text, textbox)


    def isPressed(self, pos):
        '''
        Returns whether or not the pos cords are in the button
        '''
        if (self.x <= pos[0] <= self.x + self.width and
            self.y <= pos[1] <= self.y + self.height):
            return True
        return False
