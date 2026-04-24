m = int(input())
n = int(input())

lst = []
for i in range(m, n+1):
    if int(i ** 0.5) ** 2 == i:
        lst.append(i)

if not lst:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))