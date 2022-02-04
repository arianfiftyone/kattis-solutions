
numberOfCases = int(input())


for _ in range((numberOfCases)):
    distinctCities = set()
    numberOfCities = int(input())
    for cities in range((numberOfCities)):
        differentCities = input()
        #if differentCities not in distinctCities:
        distinctCities.add(differentCities)

    print(len(distinctCities))




