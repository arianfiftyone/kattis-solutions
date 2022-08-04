
def ibem():
    numberOfCases = int(input())
    for _ in range((numberOfCases)):
        distinctCities = []
        numberOfCities = int(input())
        for cities in range((numberOfCities)):
            differentCities = input()
            if differentCities not in distinctCities:
                distinctCities.append(differentCities)

        print(len(distinctCities))

if __name__ == '__main__':
    ibem()