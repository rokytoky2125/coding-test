n = int(input())
lst = []
for j in range(n):
    s = input().split()
    lst.append(s)
    lst[-1][0] = int(lst[-1][0])
    lst[-1][2] = int(lst[-1][2])
    lst[-1][4] = int(lst[-1][4])
    if lst[j][1] == '+':
        result = lst[j][0] + lst[j][2]
        if result == lst[j][-1]:
            print('correct')
        else:
            print('wrong answer')
    elif lst[j][1] == '-':
        result = lst[j][0] - lst[j][2]
        if result == lst[j][-1]:
            print('correct')
        else:
            print('wrong answer')
    elif lst[j][1] == '*':
        result = lst[j][0] * lst[j][2]
        if result == lst[j][-1]:
            print('correct')
        else:
            print('wrong answer')
    elif lst[j][1] == '/':
        result = lst[j][0] / lst[j][2]
        if result == lst[j][-1]:
            print('correct')
        else:
            print('wrong answer')

    
    
