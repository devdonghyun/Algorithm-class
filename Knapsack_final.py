MaxProfit = 0
ans = 0


def fractional_Knapsack(n, size, profit, K):
    # n: 물건의 개수, size: 크기 리스트, profit: 가치 리스트, K: 배낭 속 남은 공간
    if K <= 0:
        return 0

    listSum = []
    newProfit, newSize = [], []

    for i in range(len(size)):
        listSum.append([size[i], profit[i], profit[i]/size[i]])
        # 가성비를 기준으로 역정렬을 수행하기 위해 리스트 생성한다.
    listSum.sort(key=lambda x: x[2], reverse=True)
    # 가성비를 기준(key)으로 역정렬을 수행하여 새로운 리스트에 저장한다.
    for i in listSum:
        newSize.append(i[0])  # 정렬된 리스트의 값 중 size에 해당하는 값들을 새로운 size 리스트에 저장한다.
        # 정렬된 리스트의 값 중 profit에 해당하는 값들을 새로운 profit 리스트에 저장한다.
        newProfit.append(i[1])

    s, p = 0, 0   # 현재까지 선택된 크기의 합과 가치의 합을 의미한다.
    for i in range(n):
        if s + newSize[i] <= K:  # 배낭에 들어갈 수 있음을 의미한다.
            p += newProfit[i]
            s += newSize[i]
        else:  # 배낭에 들어갈 수 있는 범위를 넘어섰기에 잘라서 넣는다
            p += ((K-s) * (newProfit[i]/newSize[i]))
            s = K
            break
    return p


def Knapsack(i, T):
    global MaxProfit
    global ans  # 여러 가능한 답들 중에 정답을 저장하기 위한 전역변수

    if i >= n or T <= 0:
        ans = sum(profit[i]
                  for i in range(len(x)) if x[i] == 1)
        # 모든 원소를 다 탐색했거나 배낭에 더 이상 공간이 없다면
        # 1/0으로 이루어진 x에서 선택된 값들을 모두 더해서 정답을 의미하는 변수에 저장한다.
        return
    s = sum(size[j] for j in range(i) if x[j] == 1)  # 현재 상태에서 선택된 크기의 합
    p = sum(profit[j] for j in range(i) if x[j] == 1)  # 현재 상태에서 선택된 가치의 합

    if s + size[i] <= K:  # 계속 탐색할 수 있다.
        B = fractional_Knapsack(n-(i+1), size[i+1:], profit[i+1:], T-size[i])
        if p + profit[i] + B > MaxProfit:  # 계속 탐색하면 지금보다 더 좋은 이익을 얻을 수 있다.
            x[i] = 1
            if p + profit[i] > MaxProfit:  # i번째 물건을 넣었을 때 더 많은 이익을 얻는가?
                MaxProfit = p + profit[i]  # 그렇다면 최대 이익 값을 바꿔준다.

            Knapsack(i+1, T-size[i])  # i번째 물건을 선택하고 남은 배낭의 크기와 함께 함수 호출

    B = fractional_Knapsack(n-(i+1), size[i+1:], profit[i+1:], T)
    if p + B >= MaxProfit:  # i번째 물건을 넣지 않았을 때 더 많은 이익을 얻는가?
        x[i] = 0
        Knapsack(i+1, T)


K = int(input())  # 배낭의 크기
n = int(input())  # 물건의 수
size = [int(x) for x in input().split()]  # n개의 크기
profit = [int(x) for x in input().split()]  # n개의 가치
x = [0 for i in range(n)]  # 가능한 경우들을 나타낼 리스트
Knapsack(0, K)
print(ans)
