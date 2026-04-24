n = int(input())
lst = []
for i in range(n):
    info = list(input().split())
    lst.append(info)

lst.sort(key = lambda x: (int(x[0])))

for i in lst:
    print(*i)
