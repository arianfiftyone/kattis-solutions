def isConseq():

    inputString = input()

    for index in range(len(inputString)-1):

        if inputString[index] == 's' and inputString[index+1] == 's':
            return print('hiss')
        
    print('no hiss')




if __name__ == '__main__':
    isConseq()