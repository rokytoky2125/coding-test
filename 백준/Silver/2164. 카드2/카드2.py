from collections import deque

n = int(input())

def que(n):
    dq = deque(range(1, n+1))
    while len(dq) > 1:
        dq.append(dq[1])
        dq.popleft()
        dq.popleft()
    print(dq[0])

que(n)
