import time
import random


def evaluate_n2(A, x):
    # code for O(n^2)-time function
    ans = A[0]
    for i in range(1, len(A)):
        org = x
        for j in range(1, i):
            org *= x
        ans += A[i] * org
    return ans


def evaluate_n(A, x):
    # code for O(n)-time function
    ans = A[0]
    for i in range(1, len(A)):
        ans += A[i] * (x ** i)
    return ans


random.seed()		# random 함수 초기화
n = int(input())  # n 입력받음
A = []
for i in range(n):
    A.append(random.randint(-999, 999))  # 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
x = random.randint(-99, 99)
before = time.process_time()
ans = evaluate_n2(A, x)
after = time.process_time()
print(ans)
print(after - before)

before = time.process_time()
ans = evaluate_n(A, x)
after = time.process_time()
print(ans)
print(after - before)

# evaluate_n2 호출
# evaluate_n 호출
# 두 함수의 수행시간 출력
