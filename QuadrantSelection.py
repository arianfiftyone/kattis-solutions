
def quadrantSelect():
    x = int(input())
    y = int(input())
    
    q1 = 1
    q2 = 2
    q3 = 3
    q4 = 4

    if(x > 0 and y > 0):
        print(q1)
    elif(x < 0 and y > 0):
        print(q2)
    elif(x < 0 and y < 0):
        print(q3)
    elif(x > 0 and y < 0):
        print(q4)


if __name__ == '__main__':
    quadrantSelect()
