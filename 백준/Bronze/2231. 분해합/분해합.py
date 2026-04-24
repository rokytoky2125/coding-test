n = int(input())
for m in range(1, n):
    if m + sum(map(int, str(m))) == n:
        print(m)
        break
else:
    print(0)
