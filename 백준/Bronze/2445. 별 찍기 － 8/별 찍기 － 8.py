n = int(input())

for i in range(1, n + 1):
    t = '*' * i
    p = ' ' * (2 * (n - i))
    print(t + p + t)

for i in range(n - 1, 0, -1):
    t = '*' * i
    p = ' ' * (2 * (n - i))
    print(t + p + t)
