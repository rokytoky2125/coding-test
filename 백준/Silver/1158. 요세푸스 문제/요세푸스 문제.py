from collections import deque

n, k = map(int, input().split())
dq = deque(range(1, n + 1))
result = []
while dq:
    for i in range(k-1):
        dq.rotate(-1)
    result.append(dq[0])
    dq.remove(dq[0])

print('<' + ', '.join(map(str, result)) + '>')
