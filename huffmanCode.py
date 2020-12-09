import heapq

f = [int(x) for x in input().split()]

T = []
for i in range(len(f)):
    heapq.heappush(T, (f[i], str(i)))

while len(T) > 1:
    a = heapq.heappop(T)
    b = heapq.heappop(T)
    heapq.heappush(T, (a[0]+b[0], "("+a[1]+" "+b[1]+")"))

s = heapq.heappop(T)[1]
d = [0] * len(f)
bits = 0
i = 0

while i < len(s):
    if s[i] == "(":
        bits += 1
        i += 1
    elif s[i] == ")":
        bits += 1
        i += 1
    elif s[i] == ' ':
        i += 1
    else:
        token = s[i:].split()[0]
        token = token.split("(")[0]
        token = token.split(")")[0]
        d[int(token)] = bits
        i += len(token)

print(sum([a*b for (a, b) in zip(f, d)]))
