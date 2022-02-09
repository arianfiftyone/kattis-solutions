def hn():
    integer = input()

    i = 0
    while i >= 0:
        sum = 0
        for c in range(len(integer)):
            sum += int(integer[c])
        if int(integer) % sum == 0:
            print(integer)
            break
        else:
            integer = str(int(integer) + 1)      

if __name__ == '__main__':
    hn()