import math

def tahc():

    nCases = int(input())

    for _ in range(nCases):

        data = input().split()

        v0 = float(data[0])
        angle = math.radians(float(data[1]))
        x1 = float(data[2])
        h1 = float(data[3])
        h2 = float(data[4])
        GRAVITY = 9.81
        MARGIN = 1
        
        timeAtX1 = x1 / (v0 * math.cos(angle))
        height = v0 * timeAtX1 * math.sin(angle)
        pull = (1/2) * GRAVITY * timeAtX1**2
        heightAtX1 = height - pull


        if h1 + MARGIN < heightAtX1 and heightAtX1 < h2 - MARGIN:
            print('Safe')
        else:
            print('Not Safe')


if __name__ == '__main__':
    tahc()