n = int(input())
su = 0
s = 1
for i in range(n-2, 0, -1):
    su = su + (i * s)
    s += 1
print(su)
print(3)
