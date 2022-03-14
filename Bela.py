def bela():
    data = input().split()
    nHands = int(data[0])
    domSuit = data[1]
    
    suitDom = {'A':11, 'K':4, 'Q':3, 'J':20, 'T':10, '9':14, '8':0, '7': 0}
    suitNotDom = {'A':11, 'K':4, 'Q':3, 'J':2, 'T':10, '9':0, '8':0, '7': 0}

    sum = 0

    for _ in range(nHands*4):
        plays = input()

        if plays[1] == domSuit:
            sum += suitDom[plays[0]]
        else:
            sum += suitNotDom[plays[0]]
            
    print(sum)
        




if __name__ == '__main__':
    bela()




