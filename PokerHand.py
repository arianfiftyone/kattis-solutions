from collections import Counter # dict subclass

def ph():

    # AC AD AH AS KD
    hands = Counter([hand[0:1] for hand in input().split()]) # hands = {'A':4, 'K':1}
    print(max(hands.values())) # dict_values([4, 1]), prints max = 4A
    


if __name__ == '__main__':
    ph()