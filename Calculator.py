import sys

def findNextParanthesesIndex(start, inputNR):
    for index in range(len(inputNR)):
        if inputNR[index] == '(':
            return index + start
    return None

def checkParantheses(inputNR):
    if '(' not in inputNR and len(inputNR) > 0:
        return calculator(inputNR)
    elif len(inputNR) > 0:  

        indexFirstParantheses = None
        firstFound = False

        indexLastParantheses = None
        lastFound = False
        numParatheses = 0
        for index in range(len(inputNR)):
            if inputNR[index] == '(':
                numParatheses += 1
            if inputNR[index] == ')':
                numParatheses -= 1
                
            if inputNR[index] == '(' and firstFound == False:
                indexFirstParantheses = index
                firstFound = True
            if inputNR[index] == ')' and lastFound == False and numParatheses <= 0:
                indexLastParantheses = index
                lastFound = True
                break
        calculateParantheses = inputNR[indexFirstParantheses+1:indexLastParantheses]
        checkParanthesesResult = checkParantheses(calculateParantheses)

        nextParanthesesIndex = findNextParanthesesIndex(indexLastParantheses+1, inputNR[indexLastParantheses+1:])
       
        
        if(nextParanthesesIndex != None):
            endStringResult = checkParantheses(inputNR[nextParanthesesIndex:])
            somthingelse = inputNR[indexLastParantheses+1:nextParanthesesIndex]
        else:
            endStringResult = ""
            somthingelse = inputNR[indexLastParantheses+1:]
        
        paranthesesResult = inputNR[:indexFirstParantheses] + str(checkParanthesesResult) + somthingelse + str(endStringResult)
        return calculator(paranthesesResult)

    else:
        return ""

def getArithmetic(inputNR, operation, tilInputNR):
    if operation == '+':
        return inputNR + tilInputNR
    elif operation == '-':
        return inputNR - tilInputNR
    elif operation == '*':
        return inputNR * tilInputNR
    elif operation == '/':
        return inputNR / tilInputNR
    elif operation == '.':
        return float(str(inputNR) + str(tilInputNR))

def findLastNum(inputNR, operator):
    for index in range(len(inputNR)-1, -1, -1):
        if(inputNR[index] == operator):
            return inputNR[index + 1:]

def nextNegative(start, inputNR):
    if(inputNR[0] == "-"):
        for index in range(1, len(inputNR)):
            try:
                float(inputNR[index])
            except ValueError:
                return start + index -1
        return start + len(inputNR) - 1
    else:
        return None

def calc(inputNR, operation):
    found = False
    foundIndex = 0
    firstNum_StartIndex = 0
    firstNum = 0
    lastNum_StartIndex = len(inputNR)
    lastNum = findLastNum(inputNR, operation)

    for index in range(len(inputNR)):
        try:
            float(inputNR[index])
        except ValueError:
            if(inputNR[index] == "."):
                continue
            if(found):
                if(index == foundIndex + 1 and inputNR[index] == "-"):
                    lastNum_StartIndex = nextNegative(index, inputNR[index:])
                    lastNum = inputNR[index:lastNum_StartIndex + 1]
                    break
                lastNum = inputNR[foundIndex + 1:index]
                lastNum_StartIndex = index-1
                break
            elif(found == False and inputNR[index] != operation):
                firstNum_StartIndex = index + 1
        if(index == len(inputNR) -   1):
            lastNum = inputNR[foundIndex + 1:]
            lastNum_StartIndex = index
            break

        if(inputNR[index] == operation and found == False and index != 0):
            if(index > 0):
                firstNum = inputNR[firstNum_StartIndex:index]
            found = True
            foundIndex = index
        
    if(found):
        start = inputNR[:firstNum_StartIndex]
        
        if(firstNum == "-"):
            result = lastNum
        else:
            result = str( getArithmetic( float(firstNum), operation, float(lastNum) ) )
        end = inputNR[lastNum_StartIndex+1:]

        
        if(start != None):
            result = start + result
        if(end != None):
            result = result + end
        return result
    else:
        return inputNR

def calculator(inputNR):
    while("*" in inputNR):
        inputNR = calc(inputNR, "*")
    while("/" in inputNR):
        inputNR = calc(inputNR, "/")
    while("+" in inputNR):
        inputNR = calc(inputNR, "+")
    prevInput = None
    while("-" in inputNR):
        prevInput = inputNR
        inputNR = calc(inputNR, "-")
        if(prevInput == inputNR):
            break
    return inputNR



def main():
    for line in sys.stdin:
        line = line.strip().replace(' ', '')
        print("{:.2f}".format(float(checkParantheses(line))))
            

if __name__ == '__main__':          
    main()
    

