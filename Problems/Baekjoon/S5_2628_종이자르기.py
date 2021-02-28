width, height = map(int, input().split())
n = int(input())

row = []
column = []
for _ in range(n):
    dist, index = map(int, input().split())
    if dist == 0:
        row.append(index)
    else:
        column.append(index)

row.sort()
column.sort()
row.append(height)
column.append(width)

row_max = 0
temp = 0
for element in row:
    if element-temp > row_max:
        row_max = element-temp
    temp = element

column_max = 0
temp = 0
for element in column:
    if element-temp > column_max:
        column_max = element-temp
    temp = element

print(row_max * column_max)