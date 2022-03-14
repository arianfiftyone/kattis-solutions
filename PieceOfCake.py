def poc():

    # inp = list(map(int, input().split()))
    # print(inp)

    inp = input().split()
    N = int(inp[0])
    H = int(inp[1])
    V = int(inp[2])

    newH = max(N-H, H)
    newV = max(N-V, V)

    print(newH*newV*4)

if __name__ == '__main__':
    poc()