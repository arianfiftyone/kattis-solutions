def getMegabytes(usedMegabytes, megabytes):
    leftoverMegabytes = megabytes - usedMegabytes
    return leftoverMegabytes

def availableMegabytes():
    availableMegabytes = int(input())
    nrOfMonths = int(input())
    nextMonth = availableMegabytes # refresh megabytes for the upcoming month
    for _ in range(nrOfMonths):
        spentMegabytes = int(input())
        leftoverMegabytes = getMegabytes(spentMegabytes, availableMegabytes)
        nextMonth += leftoverMegabytes

    print(nextMonth)

if __name__ == '__main__':
    availableMegabytes()