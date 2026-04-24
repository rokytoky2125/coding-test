n = int(input())

size = []

for i in range(n):
    x, y = map(int, input().split())
    size.append((x, y))

rank = [1] * n


for i in range(n):
    for j in range(n):
        if i != j:
            if size[i][0] < size[j][0] and size[i][1] < size[j][1]:
                rank[i] += 1
print(*rank)
