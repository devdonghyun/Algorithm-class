def reconstruct(S, L):
    # S, L로부터 A를 재구성해 리턴
    # 이 함수를 작성합니다~
    ans, num = [], []

    ans.append(len(S)-1-L[0])  # 리스트 처음 순서

    for i in range(len(S)):
        if ans[0] == i:
            continue
        num.append(i)

    for i in range(1, len(S)):
        if S[i] > 0:
            if S[i] != len(num)-L[i]-1:
                ans.append(num[len(num)-L[i]-1])
                num.pop(len(num)-L[i]-1)
            else:
                ans.append(num[S[i]])
                num.pop(S[i])
        else:
            ans.append(num[len(num)-L[i]-1])
            num.pop(len(num)-L[i]-1)
        print(ans)
    return ans

    # # if i == 0:
    # #     list.append(len(S)-1-L[0])  # 리스트 처음 순서
    # if i == len(S)-1:
    #     list.append(S[i])  # 리스트 마지막 순서
    # if i == S[i] and L[i] == 0:
    #     list.append(len(S)-1)  # 4일 때


# S와 L을 차례로 읽어들임
S = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
A = reconstruct(S, L)
print(A)

# 1. 본인이 작성한 알고리즘의 수행시간을 간략히 분석해보자
#
# 2. 수행시간 T(n)을 Big-O료 표기해보자
#
