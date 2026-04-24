a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
n = 0

def f(n):
    return a1 * n + a0

for i in range(n0, 101):
    if f(i) > c * i:
        print(0)
        break
    else:
        continue
else:
    print(1)
        
