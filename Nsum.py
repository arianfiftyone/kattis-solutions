
def nsum():
    inp = int(input())
    integers = input().split()
    sum = 0

    for index in range(inp):
        sum += int(integers[index])

    print(sum)


if __name__ == '__main__':
    nsum()