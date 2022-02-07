from dis import dis


def magicTrick():
    inputString = input()
    distinctChars = set()

    
    for index in range(len(inputString)):

        distinctChars.add(inputString[index])
        if len(distinctChars)-1 < index:
            return print(0)

    print(1)




if __name__ == '__main__':
    magicTrick()