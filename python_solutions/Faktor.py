def faktor():
    inp = input().split()
    firstFactor = int(inp[0])
    secondFactor = int(inp[1])
    sumFactor = (firstFactor * (secondFactor - 1)) + 1

    print(sumFactor)



if __name__ == '__main__':
    faktor()