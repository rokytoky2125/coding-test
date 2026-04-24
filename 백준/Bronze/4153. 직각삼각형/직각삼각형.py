while True:
    length = list(map(int, input().split()))
    if all(x == 0 for x in length):
        break
    else:
        values = sorted(length, reverse = True)
        a = values[0]
        b = values[1]
        c = values[2]
        if a ** 2 == b ** 2 + c ** 2:
            print("right")
        else:
            print("wrong")
