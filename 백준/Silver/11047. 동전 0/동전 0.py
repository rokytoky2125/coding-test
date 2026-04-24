import sys

n, k = map(int, input().split())
lst = []
cnt = 0
for i in range(n):
    v = int(input())
    lst.append(v)

for i in range(n-1, -1, -1):
    if k == 0:
        break
    cnt += k // lst[i]
    k %= lst[i]

sys.stdout.write(f"{cnt}")