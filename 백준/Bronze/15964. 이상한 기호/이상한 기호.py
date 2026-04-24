def func(a, b):
    c = (a + b) * (a - b)
    return c

a, b = map(int, input().split())
c = func(a, b)
print(c)
