from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, E, R):
    visited = [0] * (n + 1)
    order = 1
    q = deque([R])
    visited[R] = order
    order += 1
    
    while q:
        u = q.popleft()

        for v in sorted(E[u]): #E: 인접 리스트, E[u]: 정점 u의 인접 정점 리스트
            if visited[v] == 0:
                visited[v] = order
                order += 1
                q.append(v)
                
    return visited[1:]

n, m, r = map(int, input().split())
E = {i: [] for i in range(1, n+1)} #딕셔너리 컴프리헨션

for i in range(m):
    u, v = map(int, input().split())
    E[u].append(v) #정점 u의 이웃 리스트에 정점 v 추가
    E[v].append(u) #정점 v의 이웃 리스트에 정점 u 추가 (양방향 간선)
    
result = bfs(n, E, r)
for i in result:
    print(i)
