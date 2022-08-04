
def ratingProblems():
        
    inp = input().split()
    kJudges = int(inp[1])
    nJudges = int(inp[0])

    maxSum = 0

    for _ in range(kJudges):
        maxSum += int(input())
        
    minSum = maxSum
    maxSum = (maxSum + (nJudges-kJudges) * 3) / nJudges
    minSum = (minSum + (nJudges-kJudges) * -3) / nJudges

    print(minSum, maxSum)

if __name__ == '__main__':
    ratingProblems()
