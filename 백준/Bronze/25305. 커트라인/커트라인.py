n, k = map(int, input().split())
lst = list(input().split())
result = []
for i in lst:
    i = int(i)
    result.append(i)
result = sorted(result)
print(result[-(k)])
