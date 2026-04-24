L = int(input())
s = input()
r = 31
M = 1234567891
result = 0
j = 0
a_to_n = {}

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(26):
    letter = chr(ord('a') + i)
    a_to_n[letter] = i + 1

for i in s:
    ss = (r ** (j)) * (a_to_n[i])
    j += 1
    result += ss
result = result % M
print(result)

