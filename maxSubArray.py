def maxSubArray1(L, len):
    max = L[0]
    for i in range(len):
        for j in range(len):
            if j < i:
                continue
            sum = 0
            for k in range(i, j+1):
                sum += L[k]
            if max < sum:
                max = sum
    return max


def maxSubArray2(L, len):
    P = [0] * (len)
    P[0] = L[0]
    for i in range(1, len-1):
        P[i] = P[i-1] + L[i]
    max = L[0]
    for i in range(len):
        for j in range(len):
            if j < i:
                continue
            sum = P[j] - P[i-1]
            if max < sum:
                max = sum
    return max


def maxSubArray3(A, l, r):
    if l >= r:
        return A[l]
    m = (l + r) // 2
    L = maxSubArray3(A, l, m)
    R = maxSubArray3(A, m+1, r)

    sum1 = 0
    sum2 = 0
    max1 = A[m]
    max2 = A[m+1]
    for i in range(m, l-1, -1):
        sum1 += A[i]
        if max1 < sum1:
            max1 = sum1

    for j in range(m+1, r+1):
        sum2 += A[j]
        if max2 < sum2:
            max2 = sum2

    M = max1 + max2

    return max(L, M, R)


def maxSubArray4(A):
    n = len(A)
    S = [0] * n
    S[0] = A[0]
    for k in range(1, n):
        S[k] = max(S[k-1] + A[k], A[k])
    return max(S)


# list = [int(x) for x in input().split()]
list = [1, -1, 3, -4, 5, -4, 6, -2]
length = len(list)

print(maxSubArray1(list, length))
print(maxSubArray2(list, length))
print(maxSubArray3(list, 0, length-1))
print(maxSubArray4(list))
