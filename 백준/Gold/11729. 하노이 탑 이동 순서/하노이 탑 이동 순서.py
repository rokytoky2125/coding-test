import sys
input = sys.stdin.readline

n = int(input())
k = 2 ** n - 1
result = []

def hanoi(n, left, mid, right):
    if n == 1:
        result.append(f"{left} {right}")
    else:
        hanoi(n-1, left, right, mid)
        result.append(f"{left} {right}")
        hanoi(n-1, mid, left, right)

print(k)
if n <= 20:
    hanoi(n, 1, 2, 3)
    print('\n'.join(result))


