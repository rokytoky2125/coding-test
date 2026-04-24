from collections import Counter 

n = int(input())
cards = input().split()
m = int(input())
numbers = input().split()

card_counter = Counter(cards)
result = [card_counter[i] for i in numbers]
print(*result)
