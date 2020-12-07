def QuickSelect(L, k):
    p = L[0]
    A, M, B = [], [], []
    for x in L:
        if x < p:
            A.append(x)
        elif x > p:
            B.append(x)
        else:
            M.append(x)

    if len(A) >= k:
        return QuickSelect(A, k)
    elif len(A) + len(M) < k:
        return QuickSelect(B, k - len(A) - len(M))
    else:
        return p


def find_median_five(L):
    if len(L) == 1:
        return L[0]
    elif len(L) == 2:
        return (L[0] + L[1]) // 2
    elif len(L) == 3:
        if L[0] > L[1]:
            max = L[0]
        else:
            max = L[1]
        if max > L[2]:
            return L[2]
        else:
            return max
    elif len(L) == 4:
        if L[0] > L[1]:
            max1 = L[0]
            min1 = L[1]
        else:
            max1 = L[1]
            min1 = L[0]

        if L[2] > L[3]:
            max2 = L[3]
            min2 = L[2]
        else:
            max2 = L[2]
            min2 = L[3]
        if max1 > max2:
            median2 = max2
        else:
            median2 = max1
        if min1 > min2:
            median1 = min1
        else:
            median1 = min2
        return (median1 + median2) // 2

    else:
        if L[0] > L[1]:
            max1 = L[0]
            min1 = L[1]
        else:
            max1 = L[1]
            min1 = L[0]

        if L[2] > L[3]:
            max2 = L[2]
            min2 = L[3]
        else:
            max2 = L[3]
            min2 = L[2]

        if max1 > max2:
            if L[4] > min1:
                max1 = L[4]
            else:
                max1 = min1
                min1 = L[4]
        else:
            if L[4] > min2:
                max2 = L[4]
            else:
                max2 = min2
                min2 = L[4]

        if max1 > max2:
            if max2 > min1:
                return max2
            else:
                return min1

        else:
            if max1 > min2:
                return max2
            else:
                return min2


def MoM(L, k):
    if len(L) == 1:
        return L[0]
    A, B, M, medians = [], [], [], []

    i = 0

    while i + 4 < len(L):
        medians.append(find_median_five(L[i:i+5]))
        i += 4

    if i < len(L) and i+4 >= len(L):
        medians.append(find_median_five(L))

    mom = MoM(medians, len(medians)//2)

    for v in L:
        if v < mom:
            A.append(v)
        elif v > mom:
            B.append(v)
        else:
            M.append(v)
    if len(A) >= k:
        return MoM(A, k)
    elif len(A) + len(M) < k:
        return MoM(B, k - len(A) - len(M))
    else:
        return mom


num = input()
n, k = num.split()
n, k = int(n), int(k)
if n > 100000 or n < 1 and k > n or k < 1:
    print("wrong input")

L = list(map(int, input().split()))
if len(L) != n:
    print("wrong input")
print(QuickSelect(L, k))
print(MoM(L, k))
