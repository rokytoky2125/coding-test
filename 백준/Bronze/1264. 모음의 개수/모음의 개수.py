while True:
    line = input()
    if line == '#':
        break
    count = 0
    for ch in line:
        if ch.lower() in 'aeiou':
            count += 1
    print(count)
