def fyi():
    inp = input()

    for i in range(0, 3):
        if int(inp[i]) != 5:
            return print(0)
    print(1)

if __name__ == '__main__':
    fyi()