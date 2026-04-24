numbers = []

for i in range(9):
    number = int(input())
    numbers.append(number)
maxnum = max(numbers)
maxindex = numbers.index(maxnum)+1
print(maxnum)
print(maxindex)
