n = list(input())
i = 0
while i < len(n)-1:
    if n[i] == 'c' and n[i+1] == '=':
        n[i] = n[i] + n[i+1]
        del n[i+1]
    elif n[i] == 'c' and n[i+1] == '-':
        n[i] = n[i] + n[i+1]
        del n[i+1]
    elif i < len(n)-2 and n[i] == 'd' and n[i+1] == 'z' and n[i+2] == '=':
        n[i] = n[i] + n[i+1] + n[i+2]
        del n[i+1]
        del n[i+1]
    elif n[i] == 'd' and n[i+1] == '-':
        n[i] = n[i] + n[i+1]
        del n[i+1]
    elif n[i] == 'l' and n[i+1] == 'j':
        n[i] = n[i] + n[i+1]
        del n[i+1]
    elif n[i] == 'n' and n[i+1] == 'j':
        n[i] = n[i] + n[i+1]
        del n[i+1]
    elif n[i] == 's' and n[i+1] == '=':
        n[i] = n[i] + n[i+1]
        del n[i+1]
    elif n[i] == 'z' and n[i+1] == '=':
        n[i] = n[i] + n[i+1]
        del n[i+1]
    else:
        i += 1
print(len(n))