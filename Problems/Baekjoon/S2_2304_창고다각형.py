n = int(input())
columns = []
for _ in range(n):
    left, height = map(int, input().split())
    columns.append((left, height))
columns.sort()

# 제일 높은 기둥을 찾음
max_height = 0
max_index = 0
for i in range(n):
    if columns[i][1] > max_height:
        max_height = columns[i][1]
        max_index = i

result = 0
height = columns[0][1]
column_index = columns[0][0]
# 왼쪽부터 높은 기둥까지 넓이 계산
for i in range(1, max_index+1):
    if columns[i][1] >= height:
        result += (columns[i][0] - column_index)*height
        height = columns[i][1]
        column_index = columns[i][0]
 
# 오른쪽부터 높은 기둥까지 넓이 계산
height = columns[-1][1]
column_index = columns[-1][0]
for i in range(n-1, max_index-1, -1):
    if columns[i][1] >= height:
        result += (column_index - columns[i][0])*height
        height = columns[i][1]
        column_index = columns[i][0]

# 제일 높은 기둥이 차지하는 넓이 더해줌
result += max_height

print(result)