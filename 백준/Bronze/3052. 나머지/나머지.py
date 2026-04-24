lst = []
for i in range(10):
    n = int(input())
    s = n % 42
    if s not in lst:
        lst.append(s)
print(len(lst))
