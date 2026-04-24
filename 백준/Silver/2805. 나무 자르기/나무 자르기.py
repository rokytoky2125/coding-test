n, m = map(int, input().split())
trees = list(map(int, input().split()))

def binary_search(target, data):
    data.sort()
    start = 0
    end = max(data)
    h = 0
    
    while start <= end:
        mid = (start + end) // 2
        total = sum((d-mid) for d in data if d > mid)
        
        if total >= target:
            h = mid
            start = mid + 1
        else:
            end = mid - 1
    return(h)

print(binary_search(m, trees))
