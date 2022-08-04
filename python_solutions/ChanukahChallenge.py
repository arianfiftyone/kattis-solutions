def ch():
    data = int(input())

    for _ in range(data):
        
        dataSet = input().split()
        dataSetNr = int(dataSet[0])
        nights = int(dataSet[1])
        sumCandles = nights
        for index in range(nights):
            sumCandles += nights - index
        
        print(dataSetNr, sumCandles)
        

if __name__ == '__main__':
    ch()