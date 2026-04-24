a, b, c = map(int, input().split())
t = int(input())
c += t
while True:
    if c > 59:
        b += 1
        c -= 60
    if b > 59:
        a += 1
        b -= 60
    if a > 23:
        a = 0
    if c < 60 and b < 60 and a < 24:
        break
print(a, b, c)