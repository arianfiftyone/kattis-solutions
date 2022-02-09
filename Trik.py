def trik():

    inp = input()
    current = 1

    for index in range(len(inp)):

        if inp[index] == 'A' and current == 1:
            current = 2
        elif inp[index] == 'A' and current == 2:
            current = 1
        elif inp[index] == 'B' and current == 2:
            current = 3
        elif inp[index] == 'B' and current == 3:
            current = 2
        elif inp[index] == 'C' and current == 1:
            current = 3
        elif inp[index] == 'C' and current == 3:
            current = 1
    
    print(current)

if __name__ == '__main__':
    trik()