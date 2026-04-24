lst = []
for i in range(3):
    x = int(input())
    lst.append(x)

if lst[0] == lst[1] == lst[2] == 60:
    print('Equilateral')
elif sum(lst) == 180 and (lst[0] == lst[1] or lst[1] == lst[2] or lst[0] == lst[2]):
    print('Isosceles')
elif sum(lst) == 180 and lst[0] != lst[1] and lst[1] != lst[2] and lst[0] != lst[2]:
    print('Scalene')
else:
    print('Error')
