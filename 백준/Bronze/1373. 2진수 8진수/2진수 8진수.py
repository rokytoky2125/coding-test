n = input()
result = []

for i in range(len(n), 0, -3):
    start = max(0, i-3)
    result.append(n[start:i])
    
result.reverse()

if len(result[0]) == 2:
    result[0] = '0'+result[0]
elif len(result[0]) == 1:
    result[0] = '00'+result[0]
    
for i in range(len(result)):
    a = int(result[i][0]) * 4
    b = int(result[i][1]) * 2
    c = int(result[i][2]) * 1
    result[i] = str(a+b+c)
    
print(''.join(result))
