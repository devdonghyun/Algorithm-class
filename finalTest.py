def f3(A):
    if len(A) <= 1:
        return A
    return [A[:-1]] + f3(A[:len(A)-1])


print(f3([5, 4, 3, 2, 1]))
