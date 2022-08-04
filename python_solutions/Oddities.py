
integers = int(input())

for i in range(integers):
    currentInt = int(input())
    if (currentInt % 2 == 0):
        print(currentInt, 'is even')
    else:
        print(currentInt, 'is odd')
