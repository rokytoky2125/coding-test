n, standard = map(int, input().split())
ss = input().split()
sslist = []
find_number = []


for i in range(n):
    sslist.append(ss[i])
    if int(sslist[-1]) < standard:
        find_number.append(int(sslist[-1]))

for i in find_number:
    print(i, end = ' ')

