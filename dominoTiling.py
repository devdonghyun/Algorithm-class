A = [0, 1, 2, 5]
n = int(input())
for i in range(4, n+1):
    A.append(2*A[i-1] + A[i-3])

print(A)
