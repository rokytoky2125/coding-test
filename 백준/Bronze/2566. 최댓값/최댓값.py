# hang = []
maxs = []
maxs_column = []
for i in range(9):
    row = list(map(int, input().split()))[:9]
#     hang.append(row)
    maxs.append(max(row))
    maxs_column.append(row.index(max(row)))

value = max(maxs)
max_row = maxs.index(value)

print(value)
print(max_row+1, maxs_column[max_row]+1)