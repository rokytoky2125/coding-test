n = int(input())
lst = list(map(int, input().split()))
r = []
s = []
for i in lst:
    for j in range(1, i+1):
        if i % j == 0:
            r.append(j)
    if len(r) == 2:
        s.append(i)
    r = []
print(len(s))
