n, m = map(int, input().split())
hang1 = []
hang2 = []
hang3 = []

for i in range(n):
    greed = list(map(int, input().split()))[:m]
    hang1.append(greed)
    
for i in range(n):
    greed = list(map(int, input().split()))[:m]
    hang2.append(greed)

for i in range(n):
    row = []
    for j in range(m):
        row.append(hang1[i][j] + hang2[i][j])
    hang3.append(row)
    print(*row)