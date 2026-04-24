a, b = map(int, input().split())
s = []
d = 0
while d <= a:
    d += 1
    if a % d == 0:
        s.append(d)
if b > len(s):
    print(0)
else:
    print(s[b-1])