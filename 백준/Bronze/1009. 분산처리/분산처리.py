t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    cycle = []
    current = a % 10
    while current not in cycle:
        cycle.append(current)
        current = (current * a) % 10

    index = (b - 1) % len(cycle)
    result = cycle[index]

    print(result if result != 0 else 10)
