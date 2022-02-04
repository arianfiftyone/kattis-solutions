
numberOfCases = int(input())
sum = 0

for _ in range(numberOfCases):
    integers = input()
    lastIntPow = int(integers[-1])
    baseInt = int(integers[0:-1])

    x = (baseInt**lastIntPow)
    sum += x

print(sum)