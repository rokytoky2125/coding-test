n, k = map(int, input().split())

def factorial(n):
    s = 1
    for i in range(n, 0, -1):
        s = s * i
    return s

a = factorial(n)
b = factorial(k)
c = factorial(n-k)

print(int(a/(b * c)))
