def triangleArea():

    dimensions = input().split()
    height = int(dimensions[0])
    base = int(dimensions[1])

    res = print(base*height / 2)


if __name__ == '__main__':
    triangleArea()