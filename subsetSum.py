def print_subset(x):
    print([A[i] for i in range(len(x)) if x[i]])


def subset_sum(k):
    global printed  # 전역 변수로 사용
    v_sum = sum(A[i] for i in range(len(x)) if x[i])
    if k == len(A):
        if v_sum == S:
            print_subset(x)
            printed = 1
        elif printed == 0 and 1 not in x:
            print([])  # 출력된 적이 없고 선택된 값이 없다면 빈 리스트 출력
    else:
        # code for x[k] = 1 and x[k] = 0
        if v_sum + A[k] <= S:
            x[k] = 1
            subset_sum(k+1)
        x[k] = 0
        subset_sum(k+1)


printed = 0  # 출력한 적이 있다면 1, 아니면 0인 값
# 아래 코드는 수정하지 말고 그대로 사용할 것
A = list(set(int(x) for x in input().split()))
A.sort()
S = int(input())
x = [0]*len(A)
subset_sum(0)
