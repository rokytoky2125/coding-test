n = int(input())
min_cnt = float('inf')

for i in range(n // 5 + 1):
    rem = n - 5 * i
    if rem % 2 == 0:
        j = rem // 2
        min_cnt = min(min_cnt, i + j)

if min_cnt == float('inf'):
    print(-1)
else:
    print(min_cnt)
