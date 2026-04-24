k = int(input())
lst = [0]
for i in range(k):
    n = int(input())
    if n == 0:
        del lst[-1]
    else:
        lst.append(n)
print(sum(lst))
