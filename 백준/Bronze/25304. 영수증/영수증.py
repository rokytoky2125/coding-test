x = int(input())
n = int(input())

alist = []
blist = []
s = 0

for i in range(n):
    a, b = map(int, input().split())
    alist.append(a)
    blist.append(b)
    s += alist[-1]*blist[-1]

if x == s:
    print("Yes")
else:
    print("No")