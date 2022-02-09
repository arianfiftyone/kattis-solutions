def heartrate():
    nCases = int(input())

    for _ in range(nCases):
        inp = input().split()
        b = round(float(inp[0]), 4)
        p = round(float(inp[1]), 4)

        BPM = round(float((60*b) / p), 4)
        ABPM = round(float(60/p), 4)
        minABPM = round(BPM - ABPM, 4)
        maxABPM = round(BPM + ABPM, 4)

        print(minABPM, BPM, maxABPM)



if __name__ == '__main__':
    heartrate()
