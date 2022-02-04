n = int(input())

sum = 0

for _ in range(0, n):
    first = input().split(' ')
    sum = sum + float(first[0])* float(first[1])
print(sum)
