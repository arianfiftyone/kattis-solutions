

def zb():

    nCases = int(input())
    for _ in range(nCases):

        data = list(map(int, input().split()))
        res = 0

        for index in range(len(data)-1):

            if data[index]*2 < data[index+1]:
                res += data[index+1] - data[index]*2
        print(res)
            

if __name__ == '__main__':
    zb()