def planina():
    nIterations = int(input())
    start = 2

    for _ in range(nIterations):
        start = (start*2) - 1

    print(start*start)


if __name__ == '__main__':
    planina()



