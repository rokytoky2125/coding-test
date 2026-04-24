import sys

n = int(sys.stdin.readline())
sizes = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())

tcount = 0
for s in sizes:
    tcount += (s + t - 1) // t

pen_b = n // p
pen_s = n % p

print(tcount)
print(pen_b, pen_s)

