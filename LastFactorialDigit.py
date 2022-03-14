import math

def lfd():
    cases = int(input())

    for _ in range(cases):
        N = int(input())
        nFactorial = math.factorial(N)
        print(nFactorial % 10)




if __name__ == '__main__':
    lfd()