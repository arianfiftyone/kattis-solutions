
def batterUp():
    nBatAts = input()
    batAts = input().split()
    slugs = 0
    listScore = []
    count = 0

    for index in batAts:
        listScore.append(int(index))
    
    for scores in listScore:
        if scores >= 0:
            slugs += scores
            count += 1
            slugPercent = slugs/count

    print(slugPercent)




if __name__ == '__main__':
    batterUp()