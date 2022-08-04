
def jumboJavelin():
    nSteelrods = int(input())
    lengthOfRods = 0

    for _ in range(nSteelrods):
        differentRods = int(input())

        if lengthOfRods == 0:
            lengthOfRods += 1

        lengthOfRods += differentRods - 1

    print(lengthOfRods) 


if __name__ == '__main__':
    jumboJavelin()