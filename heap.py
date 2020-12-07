class Heap:
    def __init__(self, L=[]):
        self.A = L
        self.make_heap()

    def __str__(self):
        return str(self.A)

    def __len__(self):
        return len(self.A)

    def heapify_down(self, k, n):
        # n = 힙의 전체 노드수 [heap_sort를 위해 필요함]
        # A[k]가 힙 성질을 위배한다면, 밑으로
        # 내려가면서 힙성질을 만족하는 위치를 찾는다
        while 2*k+1 < n:           # [❓] 조건문이 어떤 뜻인가?
            L, R = 2*k + 1, 2*k + 2	 # [❓] L, R은 어떤 값?
            if L < n and self.A[L] > self.A[k]:
                m = L
            else:
                m = k
            if R < n and self.A[R] > self.A[m]:
                m = R  # m = A[k], A[L], A[R] 중 최대값의 인덱스
            if m != k:  # A[k]가 최대값이 아니라면 힙 성질 위배
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m
            else:
                break  # 왜 break할까?

    def make_heap(self):
        n = len(self.A)
        for k in range(n-1, -1, -1):  # A[n-1] → ... → A[0]
            self.heapify_down(k, n)

    def heap_sort(self):
        n = len(self.A)
        for k in range(len(self.A)-1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n = n-1
            self.heapify_down(0, n)

    def heapify_up(self, k):  # 올라가면서 A[k]를 재베치
        while k > 0 and self.A[(k-1)//2] < self.A[k]:
            self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
            k = (k-1)//2

    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A)-1)

    def delete_max(self):
        if len(self.A) == 0:
            return None
        key = self.A[0]
        self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
        self.A.pop()  # 실제로 리스트에서 delete!
        self.heapify_down(0, len(self.A))  # len(self.A) = n-1
        return key
