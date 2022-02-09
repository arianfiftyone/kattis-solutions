def pyramid():
    blocks = int(input())
    levels = 0



    while True:
        blocksUsed = (levels * 2 + 1)**2
        blocks -= blocksUsed

        if blocks < 0:
            break

        levels += 1
        
    print(levels)


        




if __name__ == '__main__':
    pyramid()