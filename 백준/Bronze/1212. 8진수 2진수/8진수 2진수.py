n = input()
num = []

for i in range(len(n)):
    d = int(n[i])
    numbers = format(d, '03b')
    num.append(numbers)

result = ''.join(num)
result = result.lstrip('0')
if result == '':
    result = '0'
print(result)