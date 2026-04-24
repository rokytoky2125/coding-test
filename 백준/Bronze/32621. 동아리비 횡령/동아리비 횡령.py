s = input()
if s.count('+') == 1:
    a, b = s.split('+')
    if a.isdigit() and b.isdigit() and a == b and a[0] != '0':
        print("CUTE")
    else:
        print("No Money")
else:
    print("No Money")
