def autori():
    inputString = input()
    newString = ''

    for char in inputString:
        if char.isupper():
            newString += char
    
    print(newString)

if __name__ == '__main__':
    autori()