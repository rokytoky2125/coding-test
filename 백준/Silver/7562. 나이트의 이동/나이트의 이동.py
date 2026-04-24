from collections import deque

n = int(input())

def knight_moves(): #행, 열 순서
    return [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]

def dfs_knight(I, sy, sx, ey, ex):
    queue = deque()
    queue.append((sy, sx, 0)) #행, 열, 횟수 순
    
    visited = [[False] * I for _ in range(I)]
    visited[sy][sx] = True
    
    moves = knight_moves()
    
    while queue:
        y, x, dist = queue.popleft() #y=행, x=열
        
        if y == ey and x == ex:
            return dist
        
        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if 0 <= ny < I and 0 <= nx < I and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx, dist + 1))
    

for i in range(n):
    I = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    print(dfs_knight(I, sy, sx, ey, ex))
