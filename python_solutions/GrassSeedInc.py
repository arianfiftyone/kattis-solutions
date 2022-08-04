def gsi():
    seedCostPerSquare = float(input())
    lawnsToSow = int(input())
    squareMeters = 0

    for index in range(lawnsToSow):
        dimensions = input().split()
        lawnWidth = float(dimensions[0])
        lawnLength = float(dimensions[1])

        squareMeters = squareMeters + (lawnWidth * lawnLength)

    costOfSow = float(squareMeters * seedCostPerSquare)
    print(costOfSow)




if __name__ == '__main__':
    gsi()