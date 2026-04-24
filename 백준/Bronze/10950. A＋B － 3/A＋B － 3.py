n = int(input())

alist = []
blist = []
s = []
    
for i in range(n):
    a, b = map(int, input().split())
    alist.append(a)
    blist.append(b)

for j in range(n):
    s.append(alist[j]+blist[j])
    print(s[j])