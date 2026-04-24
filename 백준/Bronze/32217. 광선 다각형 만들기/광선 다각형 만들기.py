n = int(input())
s = list(map(int, input().split()))
result = 180 * (n-1)
for i in range(n):
    result -= s[i]*2
print(result)
