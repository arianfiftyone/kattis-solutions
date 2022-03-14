def rbn():

    integer = int(input())
    binaryNumber = bin(integer)
    binaryNumber = binaryNumber[2:]
    reversedBinary = binaryNumber[::-1]
    print(int(reversedBinary, 2))



if __name__ == '__main__':
    rbn()       
