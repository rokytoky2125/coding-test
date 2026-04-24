import sys
from collections import Counter

numbers = []
N = int(sys.stdin.readline().strip())

for i in range(N):
    number = int(sys.stdin.readline().strip())
    numbers.append(number)

def median(numbers):
    numbers = sorted(numbers)
    if N % 2 == 0:
        result = (numbers[N // 2] + numbers[(N // 2) + 1]) / 2
    else:
        result = numbers[N // 2]
    return result

def mode(numbers):
    counts = Counter(numbers)
    max_count = max(counts.values())
    modes = sorted([k for k, v in counts.items() if v == max_count])
    if len(modes) == 1:
        result = modes[0]
    else:
        result = modes[1]
    return result

print(round(sum(numbers) / N))
print(median(numbers))
print(mode(numbers))
print(max(numbers) - min(numbers))
