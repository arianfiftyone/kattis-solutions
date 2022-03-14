import math

def ladder():
    inp = input().split()
    high = int(inp[0])
    degrees = int(inp[1])
    res = high / math.sin(math.radians(degrees))



    print(int(math.ceil(res)))



if __name__ == '__main__':
    ladder()