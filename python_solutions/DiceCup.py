def diceCup():
    dices = input().split()
    die1 = int(dices[0]) # 6
    die2 = int(dices[1]) # 6

    minimum = min(die1, die2) # 6
    maximum = max(die1, die2) # 6

    for values in range(minimum + 1, maximum + 2): # including 6+1 to excluding 6+2 = [7]
        print(values)


if __name__ == '__main__':
    diceCup()