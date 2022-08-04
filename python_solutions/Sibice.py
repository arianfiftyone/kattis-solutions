import math
N = input().split(' ')
W = int(N[1])**2
H = int(N[2])**2
hyp = math.sqrt(W + H)

for _ in range(0, int(N[0])):
    args = int(input())
    if args > hyp:
        print("NE")
    else:
        print('DA')