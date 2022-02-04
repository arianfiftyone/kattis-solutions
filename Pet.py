maxScore = 0
allContestants = 5

for persons in range(allContestants):
    currentScore = 0
    grades = input().split()
    for i in range(len(grades)):
        currentScore += int(grades[i])
    if currentScore > maxScore:
        maxScore = currentScore
        indexOfWinner = persons

print(indexOfWinner + 1, maxScore)




