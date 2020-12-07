import matplotlib.pyplot as plt
import math
import random
import timeit

##
# 여기에 세 가지 정렬함수를 위한 코드를...
##


def quick_sort(A, first, last):
    global Qc, Qs

    if first >= last:
        return
    left, right = first + 1, last
    pivot = A[first]
    while left <= right:
        while left <= last and A[left] < pivot:
            Qc += 1
            left += 1
        while right > first and A[right] > pivot:
            Qc += 1
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            Qs += 1
            left += 1
            right -= 1
            Qc += 1
    A[first], A[right] = A[right], A[first]
    Qs += 1
    quick_sort(A, first, right-1)
    quick_sort(A, right+1, last)


def merge_sort(A, first, last):
    if first >= last:
        return
    merge_sort(A, first, (first+last)//2)
    merge_sort(A, (first+last)//2+1, last)
    merge_two_sorted_lists(A, first, last)


def merge_two_sorted_lists(A, first, last):
    global Mc, Ms

    m = (first+last)//2
    i, j = first, m+1
    B = []
    while i <= m and j <= last:
        if A[i] <= A[j]:
            Mc += 1
            B.append(A[i])
            Ms += 1
            i += 1
        else:
            Mc += 1
            B.append(A[j])
            Ms += 1
            j += 1
    for k in range(i, m+1):
        B.append(A[k])
        Ms += 1
    for k in range(j, last+1):
        B.append(A[k])
        Ms += 1
    for i in range(first, last+1):
        A[i] = B[i-first]
        Ms += 1


def heapify_down(A, k, n):
    global Hc, Hs

    while 2*k+1 < n:
        L, R = 2*k + 1, 2*k + 2
        if L < n and A[L] > A[k]:
            Hc += 1
            m = L
        else:
            Hc += 1
            m = k
        if R < n and A[R] > A[m]:
            Hc += 1
            m = R
        if m != k:
            A[k], A[m] = A[m], A[k]
            Hs += 1
            k = m
        else:
            break


def make_heap(A):
    n = len(A)
    for k in range(n-1, -1, -1):
        heapify_down(A, k, n)
    return A


def heap_sort(A):
    global Hs
    A = make_heap(A)
    n = len(A)
    for k in range(n-1, -1, -1):
        A[0], A[k] = A[k], A[0]
        Hs += 1
        n = n-1
        heapify_down(A, 0, n)

# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#


def check_sorted(A):
    for i in range(n-1):
        if A[i] > A[i+1]:
            return False
    return True


#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

list_N, quickSortList, mergeSortList, heapSortList = [], [], [], []
random.seed()
for i in range(8):
    n = int(input())
    list_N.append(n)
    A = []
    for i in range(n):
        A.append(random.randint(-1000, 1000))
    B = A[:]
    C = A[:]
    print("")
    print("Quick sort:")
    print("time =", timeit.timeit(
        "quick_sort(A, 0, n-1)", globals=globals(), number=1))
    print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
    print("Merge sort:")
    print("time =", timeit.timeit(
        "merge_sort(B, 0, n-1)", globals=globals(), number=1))
    print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

    print("Heap sort:")
    print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
    print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

    # 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
    assert(check_sorted(A))
    assert(check_sorted(B))
    assert(check_sorted(C))

    log10List.append(3*n*log10(n))
    quickSortList.append(Qc+Qs)
    mergeSortList.append(Mc+Ms)
    heapSortList.append(Hc+Hs)


plt.plot(list_N, quickSortList, label='Quick Sort', color='r')
plt.plot(list_N, mergeSortList, label='Merge Sort', color='g')
plt.plot(list_N, heapSortList, label='Heap Sort', color='b')
plt.plot(list_N, log10List, label='3nlogn', color='y')
plt.xlabel('n')
plt.ylabel('number of comparisons + swaps + moves')
plt.legend()
plt.show()


if last-first+1 <= 10:
    for i in range(1, len(A)):
        j = i-1
        while j >= 0 and A[j] > A[j+1]:
            Mc += 1
            A[j], A[j+1] = A[j+1], A[j]
            Ms += 1
            j = j-1
    return
