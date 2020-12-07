def reconstruct(B):
    # B로부터 A를 재구성해 리턴
    # 이 함수를 작성합니다~
    ans, num = [], []

    for i in range(len(B)):
        ans.append(0)
        num.append(i)

    for i in range(len(B)-1, -1, -1):
        pos = 0
        for _ in range(B[i]):
            pos += 1
        ans[i] = num[pos]
        del num[pos]

    return ans


B = [int(x) for x in input().split()]
A = reconstruct(B)
print(A)
