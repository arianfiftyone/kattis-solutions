def transitWoes():
    data = input().split()
    s = int(data[0])
    t = int(data[1])
    n = int(data[2])
    bool = False

    walk = list(map(int, input().split()))
    bus = list(map(int, input().split()))
    wait = list(map(int, input().split()))

    for index in range(len(wait)):

        if (walk[index] + bus[index] + wait[index] + walk[-1] + s) <= t:
            bool = TrueW


    if bool:
        print('yes')
    else:
        print('no')

if __name__ == '__main__':
    transitWoes()