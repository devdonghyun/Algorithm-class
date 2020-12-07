import heapq


def huffmanCode():
    H = []
    for x in range(n):
        heappush(H, (f[x], 'x'))

    while len(H) > 1:
        a = heappop(H)
        b = heappop(H)
        heappush(H, a.f + b.f, '(a.x b.x)')
    tree_string = heappop(H)[1]
