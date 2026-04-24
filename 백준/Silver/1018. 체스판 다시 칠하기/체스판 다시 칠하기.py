n, m = map(int, input().split())
board = []
ss = []

for _ in range(n):
    board.append(list(input()))  # 2차원 저장


for i in range(n - 7):
    for j in range(m - 7):
        k1 = 0  # 첫번째칸: 'B' 
        k2 = 0  # 첫번째칸: 'W'
        for x in range(8):
            for y in range(8):
                current = board[i + x][j + y]
                if (x + y) % 2 == 0:
                    if current != 'B':
                        k1 += 1
                    if current != 'W':
                        k2 += 1
                else:
                    if current != 'W':
                        k1 += 1
                    if current != 'B':
                        k2 += 1
        ss.append(min(k1, k2))

print(min(ss))
