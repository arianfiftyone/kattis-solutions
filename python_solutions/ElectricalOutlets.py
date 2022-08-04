def eo():

    nCases = int(input())

    for _ in range(nCases):
        inputData = input().split()
        powerStrips = list(map(int, inputData[1:])) # [2, 3, 4]
        nPowerStrips = len(powerStrips) # 3
        nOutlets = sum(powerStrips) # 2 + 3 + 4 = 9
        nApplicances = (nOutlets - nPowerStrips) + 1 # (9 - 3) + 1 = 7, ez rly

        print(nApplicances)


if __name__ == '__main__':
    eo()