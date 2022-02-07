def nastyHacks():
    nCases = int(input())

    for _ in range(nCases):
        business = input().split()
        r = int(business[0])
        e = int(business[1])
        c = int(business[2])

        if e-c == r:
            print('does not matter')
        elif e-c > r:
            print('advertise')
        else:
            print('do not advertise')





if __name__ == '__main__':
    nastyHacks()