import math


def matrix_mult():
    for d in range(n):
        for i in range(1, n-d+1):
            j = i + d
            if i == j:
                C[i][j] = 0
                continue
            C[i][j] = math.inf  # math module에서 제공하는 매우 큰 정수
            for k in range(i, j):
                cost = C[i][k] + C[k+1][j] + P[i-1] * P[k] * P[j]
                if C[i][j] > cost:
                    C[i][j] = cost
    start = 1
    end = n
    return C[start][end]


n = int(input())  # n = 행렬 갯수, M_0부터 행렬시작임을 주의!
mat = n+1
P = [int(x) for x in input().split()]  # M_i = p_i x p_{i+1}
C = [[0]*mat for _ in range(mat)]  # 비용을 저장할 2차원 리스트 C 초기화
min_cost = matrix_mult()
print(min_cost)
print(C[0][1])
print(C)
