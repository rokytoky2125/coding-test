from collections import deque
#bfs
N, M, V = map(int, input().split()) #정점 개수, 간선 개수, 시작 번호

#인접리스트 그래프 만들기
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, N+1):
    graph[i].sort()

def bfs(start, graph, visited):
    queue = deque([start]) #큐 만들기: 탐색 목록
    visited[start] = True
    
    while queue: #큐가 없어질 때까지 반복
        node = queue.popleft()
        print(node, end = ' ')
        
        for nxt in graph[node]: #연결선 구성하는 원소들 모두 점검할 때까지 반복
            if not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = True

#dfs
def dfs(start, graph, visited):
    visited[start] = True
    print(start, end = ' ')
    
    for nxt in graph[start]:
        if not visited[nxt]:
            dfs(nxt, graph, visited)


#노드(정점) 방문 목록 만들기 (1부터 N까지)
visited = [False] * (N + 1)
dfs(V, graph, visited)
print()
visited = [False] * (N + 1)
bfs(V, graph, visited)

