
def abracadabra():
    N = int(input())
    string = 'Abracadabra'
    for index in range(N):
        newString = str(index+1) + ' ' + string
        print(newString)
        
if __name__ == '__main__':
    abracadabra()