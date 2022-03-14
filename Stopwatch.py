
def sw():

    nButtonPresses = int(input())
    isPressed = False # a press alternates between start and stop
    accumulatedTime = 0
    previousTime = 0

    for _ in range(nButtonPresses):
        currentTime = int(input()) # 7
        
        if isPressed == True:
            accumulatedTime += currentTime - previousTime
            isPressed = False
        else:
            previousTime = currentTime
            isPressed = True


    if isPressed:
        print('Still running')
    else:
        print(accumulatedTime)



if __name__ == '__main__':
    sw()