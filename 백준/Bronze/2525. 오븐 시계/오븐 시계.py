h, m = map(int, input().split())
t = int(input())

m += t
while True:
    if m > 59:
        h += 1
        m -= 60
        if h > 23:
            h = 0
    if m < 59:
        break

print(h, m)