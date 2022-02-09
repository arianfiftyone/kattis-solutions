def filip():
    inp = input().split()
    firstNumber = inp[0][::-1]
    secondNumber = inp[1][::-1]
    print(max(firstNumber, secondNumber))

if __name__ == '__main__':
    filip()