def sc():
    width = int(input())
    nPieces = int(input())
    totalArea = 0

    for _ in range(nPieces):
        subCakes = list(map(int, input().split()))

        totalArea += subCakes[0]*subCakes[1]

        length = totalArea/width

    print(int(length))





if __name__ == '__main__':
    sc()