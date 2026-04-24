lst = []
for i in range(28):
    n = int(input())
    lst.append(n)
lst.sort()

for i in range(1, 31):
    if i not in lst:
        print(i)