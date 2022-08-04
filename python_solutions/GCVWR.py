# Gross combined vehicle weight rating = max haul weight incl. truck

def haul():

    # GCWV, weight of truck, nr of items to bring
    G, T, N = map(int, input().split())
    items = input().split()
    allowedWeight = int((G - T) * 0.9)
    itemWeight = 0

    for index in range(len(items)):
        itemWeight += int(items[index])
        haulWeight = allowedWeight - itemWeight
    print(haulWeight)


if __name__ == '__main__':
    haul()