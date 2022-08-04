N = input().split(' ')
king = 1
queen = 1
rooks = 2
bishops = 2
knights = 2
pawns = 8

print(king-int(N[0]), queen-int(N[1]), rooks-int(N[2]), bishops-int(N[3]), knights-int(N[4]), pawns-int(N[5]))
