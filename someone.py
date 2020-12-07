def two_max(A, left, right, depth):
    if left == right:
        return A[left], None
    if len(A) == 2:
        if A[left] >= A[right]:
            return A[left], A[right]
        else:
            return A[right], A[left]
    mid = (left+right)//2

    M1, m1 = two_max(A[left:mid+1], left - left, mid - left, depth+1)
    print("L1:", M1, "L2:", m1)
    M2, m2 = two_max(A[mid+1:right+1], (mid+1)-(mid+1), right-(mid+1), depth+1)
    print("R1:", M2, "R2:", m2)

    if M1 >= M2:
        if M2 >= m1:
            print(M1, M2)
            return M1, M2
        else:
            print(M1, m1)
            return M1, m1
    else:
        if M1 >= m2:
            print(M2, m1)
            return M2, M1
        else:
            print(M2, m2)
            return M2, m2


A = [int(i) for i in input().split()]
M, m = two_max(A, 0, len(A)-1, 1)
print(M, m)
