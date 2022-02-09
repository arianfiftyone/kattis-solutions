def homework():
    line = input().split(';')
    nProblems = 0

    for index in line:
        if '-' in index:
            atLeastTwo = list(map(int, index.split('-'))) # 1-5 = [1, 5]
            nProblems += (atLeastTwo[1] - atLeastTwo[0]) + 1 # (5-1) + 1 = 5
        else:
            nProblems += 1

    print(nProblems)


if __name__ == '__main__':
    homework()