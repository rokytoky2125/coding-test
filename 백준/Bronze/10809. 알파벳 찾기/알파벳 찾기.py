import string

s = input()
alphabet = list(string.ascii_lowercase)
lst = []

for i in range(26):
    lst.append(s.find(alphabet[i]))
print(*lst)
