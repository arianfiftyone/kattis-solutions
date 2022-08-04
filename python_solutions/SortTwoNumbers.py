
def sortTwoNumbers():

    data = input().split()
    firstInt = int(data[0])
    secondInt = int(data[1])

    print(min(firstInt, secondInt), max(firstInt, secondInt))


if __name__ == '__main__':
    sortTwoNumbers()