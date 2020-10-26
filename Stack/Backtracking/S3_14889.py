from itertools import combinations

n = int(input())
power_list = [list(map(int, input().split())) for _ in range(n)]

id_list = [i for i in range(n)]
coms = combinations(id_list, n//2)

result = int(1e9)
for com in coms:
    temp_start = 0
    temp_link = 0
    com_coms = combinations(com, 2)
    for com_com in com_coms:
        temp_start += power_list[com_com[0]][com_com[1]]
        temp_start += power_list[com_com[1]][com_com[0]]
    
    com_minus = set(id_list) - set(com)
    com_minus_coms = combinations(com_minus, 2)
    for com_minus_com in com_minus_coms:
        temp_link += power_list[com_minus_com[0]][com_minus_com[1]]
        temp_link += power_list[com_minus_com[1]][com_minus_com[0]]

    temp = abs(temp_link - temp_start)
    if temp == 0:
        result = temp
        break
    if temp < result:
        result = temp

print(result)