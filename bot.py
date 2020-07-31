# bot.py

'''
This will be the program for a chess AI
Note: Requires the pieces.py file to work
'''

board = {}
for row in range(1, 9):
    for col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        board[col + str(row)] = None


def eval(board):
    '''
    Evaluate the given position by board and returns the best move
    as a string of 'originalposition' + 'destinationposition'

    Ex: Pawn e4 opening would be e2e4  
    '''
    return
