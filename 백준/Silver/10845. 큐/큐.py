import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()
output = []

for _ in range(n):
    order = input()
    if order.startswith('push'):
        queue.append(order.split()[1])
    elif order.startswith('pop'):
        if queue:
            output.append(queue.popleft())
        else:
            output.append('-1')
    elif order.startswith('size'):
        output.append(str(len(queue)))
    elif order.startswith('empty'):
        output.append('0' if queue else '1')
    elif order.startswith('front'):
        output.append(queue[0] if queue else '-1')
    elif order.startswith('back'):
        output.append(queue[-1] if queue else '-1')

print('\n'.join(output))

