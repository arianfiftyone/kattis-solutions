
def fb():
    integers = input().split()

    X = int(integers[0])
    Y = int(integers[1])
    N = int(integers[2]) 

    for index in range(1, N+1): 
        if index % X == 0 and index % Y == 0:
             print('FizzBuzz')
        elif index % X == 0:
            print('Fizz')
        elif index % Y == 0:
            print('Buzz')
        else: 
            print(index)



if __name__ == '__main__':
    fb()