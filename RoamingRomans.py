import math

def rr():
    nEnglishMiles = float(input())

    romanConverter = round((1000 * (5280/4854)) * nEnglishMiles)
    

    print(int(romanConverter))


    




if __name__ == '__main__':
    rr()