
def zamka():
    l = int(input())
    d = int(input())
    x = int(input())

    lowest = findLowest(l, d, x)
    highest = findHighest(l, d, x)
    print(lowest)
    print(highest)

def findLowest(l, d, x):
    n = l

    while n <= d:
        if digitSum(n) == x:
            return n
        n += 1

    return


def findHighest(l, d, x):
    m = d
    
    while m >= l:
        if digitSum(m) == x:
            return m
        m -= 1

    return


def digitSum(digits):
    print('digitsum')
    sum = 0
    while digits > 9:

        sum += (digits % 10)
        digits = digits // 10
    
    sum += digits
    return sum



if __name__ == '__main__':
    zamka()









    
