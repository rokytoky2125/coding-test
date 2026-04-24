k = int(input())
result = []
output = []
for i in range(k):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    
    queue = [(i, p) for i, p in enumerate(priorities)]
    count = 0
    
    while queue:
        current = queue.pop(0)
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            count += 1
            if current[0] == m:
                output.append(count)
                break
            
for i in output:
    print(i)
