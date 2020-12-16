def quick_sort(A, first, last):
    if last-first+1 <= 10:
        for i in range(first+1, last+1):
            j = i-1
            while j >= first and A[j] > A[j+1]:

                A[j], A[j+1] = A[j+1], A[j]

                j = j-1
        return

    left, right = first + 1, last
    pivot = A[first]
    while left <= right:
        while left <= last and A[left] < pivot:
            left += 1
        while right > first and A[right] > pivot:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1

    A[first], A[right] = A[right], A[first]
    print(A)
    quick_sort(A, first, right-1)
    quick_sort(A, right+1, last)


A = [4, 2, 5, 8, 6, 2, 3, 7, 10]
print(quick_sort(A, 0, len(A)-1))
