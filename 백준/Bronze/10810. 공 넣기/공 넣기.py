n, m = map(int, input().split())
lst = [0]*n
for i in range(m):
    a, b, c = map(int, input().split())
    for j in range(a-1, b):
        lst[j] = c
print(*lst)
