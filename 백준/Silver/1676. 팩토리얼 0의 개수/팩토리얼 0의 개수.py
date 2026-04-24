n = int(input())
def factorial(n):
    s = 1
    for i in range(n, 0, -1):
        s = s * i
    return s

a = factorial(n)
count = 0

for i in range(1, len(str(a))):
    if str(a)[-i] == '0':
        count += 1
    else:
        break
print(count)