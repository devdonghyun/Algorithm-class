W = int(input())
words = input().split()
# code below
length = len(words)
DP = [[0] * length for i in range(length)]
cost = [0 for i in range(length)]


for i in range(length):
    if i == length-1:
        break
    DP[i][i] = W - len(words[i])
    for j in range(i+1, length):
        DP[i][j] = DP[i][j-1] - len(words[j]) - 1

        if j-i == 1:
            j -= 1
            if DP[i][j] < 0:
                DP[i][j] = float('inf')
            else:
                DP[i][j] = DP[i][j] ** 3

            j += 1
            if DP[i][j] < 0:
                DP[i][j] = float('inf')
            else:
                DP[i][j] = DP[i][j] ** 3
        else:
            if DP[i][j] < 0:
                DP[i][j] = float('inf')
            else:
                DP[i][j] = DP[i][j] ** 3

        if i == length-2 and j == length-1:
            i += 1
            DP[i][i] = W - len(words[i])
            if DP[i][j] < 0:
                DP[i][j] = float('inf')
                break
            else:
                DP[i][j] = DP[i][j] ** 3
                break

for i in range(length-1, -1, -1):
    cost[i] = DP[i][length-1]
    for j in range(length-1, i, -1):
        if DP[i][j-1] == float('inf'):
            continue

        prevCost = cost[j] + DP[i][j-1]
        if cost[i] > prevCost:
            cost[i] = prevCost

print(cost[0])
