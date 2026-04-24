import sys
input = sys.stdin.readline

m = int(input())
s = set()
for i in range(m):
    order = input().split()
    if order[0] == 'add':
        s.add(int(order[1]))
    elif order[0] == 'remove':
        s.discard(int(order[1]))
    elif order[0] == 'check':
        print(1 if int(order[1]) in s else 0)
    elif order[0] == 'toggle':
        if int(order[1]) in s:
            s.discard(int(order[1]))
        else:
            s.add(int(order[1]))
    elif order[0] == 'all':
        s = set(range(1, 21))
    elif order[0] == 'empty':
        s = set()

