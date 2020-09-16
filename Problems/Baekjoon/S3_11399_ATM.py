n = int(input())
sum_list = [0]*n
time_list = sorted(list(map(int, input().split())))

for i in range(len(time_list)):
    if i == 0:
        sum_list[0] = time_list[0]
    else:
        sum_list[i] = sum_list[i-1] + time_list[i]

print(sum(sum_list))