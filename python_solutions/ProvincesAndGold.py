def pog():

    # Gold, silver, copper
    G, S, C = map(int, input().split())
    victoryCard, treasureCard = '', ''
    funds = G*3 + S*2 + C*1

    # determine coin
    if funds >= 6:
        treasureCard = 'Gold'
    elif funds >= 3:
        treasureCard = 'Silver'
    else:
        treasureCard = 'Copper'

    # determine property
    if funds >= 8:
        victoryCard = 'Province'
    elif funds >= 5:
        victoryCard = 'Duchy'
    elif funds >= 2:
        victoryCard = 'Estate'
    
    if funds < 2:
        print(treasureCard)
    else:
        print(victoryCard, 'or', treasureCard)

    


if __name__ == '__main__':
    pog()