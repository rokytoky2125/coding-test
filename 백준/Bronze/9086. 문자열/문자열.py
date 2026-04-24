n = int(input())
slist = []

for i in range(n):
    s = input()
    slist.append(s)
    ss = slist[-1]
    print(ss[0]+ss[-1])