from collections import Counter

s = list(input().upper())
counter = Counter(s)
sorted_items = sorted(counter.items(), key=lambda x: -x[1])
first_char = sorted_items[0][0]
if len(sorted_items) > 1 and sorted_items[0][1] == sorted_items[1][1]:
    print("?")
else:
    print(first_char)
