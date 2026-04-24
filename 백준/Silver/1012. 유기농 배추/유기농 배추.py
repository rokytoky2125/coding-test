import sys
input = sys.stdin.readline

from collections import deque

T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    def bfs(x, y):
        queue = deque() #방문할 곳을 저장하는 큐 생성
        queue.append((x, y)) #큐에 튜플형태로 저장
        arr[y][x] = 0 #방문 처리
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)] #상하좌우 이동
        
        while queue:
            cx, cy = queue.popleft() #큐에서 가장 먼저 들어온 위치 꺼내기
            
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy #다음 이동 위치
                
                if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 1:
                    arr[ny][nx] = 0
                    queue.append((nx, ny))
                    
    count = 0
    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1:
                bfs(x, y)
                count += 1
    print(count)
