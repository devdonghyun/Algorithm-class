def pin(A):
    # code here

    k = 0
    count = 0
    for i in range(1, len(A)):
        if A[k][1] < A[i][0]:
            print("k:", k, "A[k][1]:", A[k][1])
            count += 1
            k = i

    return count+1


n = int(input())
list_pin = [tuple(map(int, input().split()))for i in range(n)]
list_pin.sort(key=lambda x: x[1])

print(pin(list_pin))
