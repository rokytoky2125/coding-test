n = int(input())
array = [[0]*100 for _ in range(100)]
result = 0

for k in range(n):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            array[i][j] = 1

for i in range(100):
    for j in range(100):
        if array[i][j] == 1:
            result += 1

print(result)