
def abracadabra():
    N = int(input())
    ABRACADABRA = 'Abracadabra'
    for index in range(N):
        outputString = str(index+1) + ' ' + ABRACADABRA
        print(outputString) # print output every loop
        
if __name__ == '__main__':
    abracadabra()