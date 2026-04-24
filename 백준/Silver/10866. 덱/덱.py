from collections import deque

n = int(input())
dq = deque()
result = []

for i in range(n):
    order = input().split()
    if order[0] == 'push_back':
        dq.append(order[1])
    elif order[0] == 'push_front':
        dq.appendleft(order[1])
    elif order[0] == 'pop_back':
        result.append(dq.pop())  if dq else result.append(-1)
    elif order[0] == 'pop_front':
        result.append(dq.popleft()) if dq else result.append(-1)
    elif order[0] == 'size':
        result.append(len(dq))
    elif order[0] == 'empty':
        result.append(0 if dq else 1)
    elif order[0] == 'front':
        result.append(dq[0] if dq else -1)
    elif order[0] == 'back':
        result.append(dq[-1] if dq else -1)

for i in result:
    print(i)
