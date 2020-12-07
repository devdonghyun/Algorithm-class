W = int(input())
words = input().split()
# code below
length = len(words)
DP = [[0] * length for i in range(length)]
cost = [0 for i in range(length)]

for i in range(length):
    DP[i][i] = W - len(words[i])
    for j in range(i+1, length):
        blank = 0
        blank += 1
        DP[i][j] = DP[i][j-1] - len(words[j]) - blank


for i in range(length):
    for j in range(i, length):
        print("next:", i, j)
        if DP[i][j] < 0:
            DP[i][j] = float('inf')
        else:
            DP[i][j] = DP[i][j] ** 3

for i in range(length-1, -1, -1):
    cost[i] = DP[i][length-1]
    for j in range(length-1, i, -1):
        if DP[i][j-1] == float('inf'):
            continue

        prevCost = cost[j] + DP[i][j-1]
        if cost[i] > prevCost:
            cost[i] = prevCost

print(cost)

print(DP)
