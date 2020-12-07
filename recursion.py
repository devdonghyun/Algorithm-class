def sum(n):
    if n <= 1:
        return n
    return n + sum(n-1)


n = int(input("n = "))
print(sum(n))


def sum_2(a, b):  # return a + (a+1) + ... + b
    if a > b:
        return 0
    if a == b:
        return a
    m = (a+b)//2
    return sum_2(a, m) + sum_2(m+1, b)


a = int(input("a = "))
b = int(input("b = "))
print(sum_2(a, b))


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


def find_max(A, n):
    if n == 1:
        if A[0] > A[n]:
            max = A[0]
            return max
        else:
            max = A[n]
            return max
    else:
        curr_max = find_max(A, n-1)
        if A[n] > curr_max:
            max = A[n]
            return max
        else:
            max = curr_max
            return max


A = [1, 3, 5, 4, 2]
n = len(A) - 1
print(find_max(A, n))


def reverse(A, start, stop):  # A[start] ... A[stop-1] 을 역전
    if start < stop-1:  # 2개 이상의 값이 있는 경우만 의미 있으므로
        A[start], A[stop-1] = A[stop-1], A[start]
        reverse(A, start+1, stop-1)


A = [1, 2, 3, 4, 5, 6]
print(A)
reverse(A, 0, len(A))
print(A)
