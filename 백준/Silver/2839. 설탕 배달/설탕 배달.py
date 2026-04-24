n = int(input())
cnt = float('inf')

for i in range(n // 5 + 1):
    rem = n - (5 * i)
    if rem % 3 == 0:
        j = rem // 3
        cnt = min(cnt, i + j)

if cnt == float('inf'):
    print(-1)
else:
    print(cnt)
