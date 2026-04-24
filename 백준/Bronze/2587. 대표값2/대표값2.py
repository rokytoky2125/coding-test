lst = []
for i in range(5):
    n = int(input())
    lst.append(n)
lst = sorted(lst)
print(sum(lst)//5)
print(lst[2])
