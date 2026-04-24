N = int(input())

layer = 1
max_num = 1

while N > max_num:
    max_num += 6 * layer
    layer += 1

print(layer)