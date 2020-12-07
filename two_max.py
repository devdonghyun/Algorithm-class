def two_max(A, left, right):

    if left == right:
        return A[left], None

    mid = (left + right) // 2
    L1, L2 = two_max(A, left, mid)
    print("L1:", L1, "L2:", L2)
    R1, R2 = two_max(A, mid+1, right)
    print("R1:", R1, "R2:", R2)

    if R2 == None:
        if L1 > R1:
            M = L1
            if L2 != None:
                if L2 > R1:
                    m = L2
                else:
                    m = R1
            else:
                m = R1
            print("M: ", M, "m: ", m)
            print("L2-: ", L2, "R2-: ", R2)
        else:
            M = R1
            m = L1
            print("M: ", M, "m: ", m)
        return M, m

    if L1 > R1:
        M = L1
        min1 = R1
    else:
        M = R1
        min1 = L1
    if L2 > R2:
        min2 = L2
    else:
        min2 = R2

    if min1 > min2:
        m = min1
    else:
        m = min2
    print("L1:", L1, "R1:", R1)
    print("L2:", L2, "R2:", R2)
    return M, m


A = list(map(int, input().split()))
# M, m = two_max(A, 0, len(A)-1)
M, m = two_max(A, 0, len(A)-1)
# print(m, M)
print(M, m)
