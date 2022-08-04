def greetings():
    inputString = input()

    newString = 'h'
    for index in range(len(inputString)):

        if inputString[index] == 'e':
            newString += 'ee'
    newString += 'y'
    print(newString)







if __name__ == '__main__':
    greetings()