n = int(input())
ss = input().split()
find = int(input())
find_number = 0
sslist = []

for i in range(n):
    sslist.append(ss[i])
    if int(sslist[-1]) == find:
        find_number += 1
        
print(find_number)
