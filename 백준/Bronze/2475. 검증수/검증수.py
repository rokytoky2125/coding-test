lst = list(map(int, input().split()))
s = 0
r = 0
for i in lst:
    s += i ** 2
r = s % 10
print(r)
