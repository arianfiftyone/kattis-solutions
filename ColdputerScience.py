
numberOfTemps = int(input())
temps = input().split()
countNegatives = 0

for i in range(numberOfTemps):
    if (int(temps[i]) < 0):
        countNegatives += 1
    
print(countNegatives)

