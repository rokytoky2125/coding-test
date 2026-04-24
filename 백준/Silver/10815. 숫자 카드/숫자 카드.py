n1 = int(input())
lst1 = list(map(int, input().split()))
n2 = int(input())
lst2 = list(map(int, input().split()))
set1 = set(lst1)
for i in lst2:
    if i in set1:
        print('1', end =' ')
    else:
        print('0', end = ' ')
