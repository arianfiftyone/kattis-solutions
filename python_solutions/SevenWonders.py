def sw():

    cards = (input())

    TCG = {'T':0, 'C':0, 'G':0}

    for index in range(len(cards)):

        if cards[index] in TCG:
            TCG[cards[index]] += 1
    
    sum = 0
    min = 100
    for keys in TCG:

        if TCG[keys] < min:
            min = TCG[keys]
        
        sum += TCG[keys]**2

    print(sum + min * 7)
            








if __name__ == '__main__':
    sw()