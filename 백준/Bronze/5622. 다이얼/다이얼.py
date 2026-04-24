n = list(input())
s = []
list2 = ['A', 'B', 'C']
list3 = ['D', 'E', 'F']
list4 = ['G', 'H', 'I']
list5 = ['J', 'K', 'L']
list6 = ['M', 'N', 'O']
list7 = ['P', 'Q', 'R', 'S']
list8 = ['T', 'U', 'V']
list9 = ['W', 'X', 'Y', 'Z']

for i in range(len(n)):
    if n[i] in list2:
        s.append(3)
    elif n[i] in list3:
        s.append(4)
    elif n[i] in list4:
        s.append(5)
    elif n[i] in list5:
        s.append(6)
    elif n[i] in list6:
        s.append(7)
    elif n[i] in list7:
        s.append(8)
    elif n[i] in list8:
        s.append(9)
    elif n[i] in list9:
        s.append(10)
print(sum(s))