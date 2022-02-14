import math
import sys

def winnerMultGame(data):

    turns = 0
    turn = False
    while data > 1:
        if turn:
            data = data/2
            turn = False
        else:
            data = math.ceil(data/9)
            turn = True

        turns += 1

    if turns % 2:
        return print('Stan wins.')
    else:
        return print('Ollie wins.')


if __name__ == '__main__':
    for data in sys.stdin:
        winnerMultGame(int(data))