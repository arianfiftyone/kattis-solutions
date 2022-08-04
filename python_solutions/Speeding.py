def maxMilesPerHour():

    nPhotos = int(input())
    prevHour, prevMile = list(map(int, input().split()))
    maxVelocity = 0

    for _ in range(nPhotos-1):
        currHour, currMile = list(map(int, input().split()))

        deltaHour = currHour - prevHour
        deltaMile = currMile - prevMile

        velocity = deltaMile // deltaHour # floor
        maxVelocity = max(velocity, maxVelocity)
        
        prevHour = currHour
        prevMile = currMile

    print(maxVelocity)


if __name__ == '__main__':
    maxMilesPerHour()