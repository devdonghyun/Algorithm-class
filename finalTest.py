def do_something(A,k):
    A.sort()
    for x in A:
        if BS(A,0,len(A), k-x)