def jackO():
    threeInts = input().split()
    uniqueDesignsPossible = 1

    for index in range(len(threeInts)):
        uniqueDesignsPossible *= int(threeInts[index])

    print(uniqueDesignsPossible)


if __name__ == '__main__':
    jackO()