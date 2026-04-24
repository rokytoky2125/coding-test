words = []
length = []
for i in range(5):
    s = list(input())
    words.append(s)
    length.append(len(s))

for i in range(max(length)):
    for j in range(5):
        if i >= len(words[j]): ##
            continue
        print(words[j][i], end = '')
