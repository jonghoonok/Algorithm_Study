def next_index(i):
    if i == 0:
        return 5
    elif i == 1:
        return 3
    elif i == 2:
        return 4
    elif i == 3:
        return 1
    elif i == 4:
        return 2
    else:
        return 0
        
        
def side_max(index, arr):
# 0, 5를 고르면 1~4 인덱스를 이용해서 조합
    if index == 0 or index == 5:
        return max(arr[1], arr[2], arr[3], arr[4])
# 1, 3을 고르면 0, 2, 4, 5인덱스를 이용해서 조합
    elif index == 1 or index == 3:
        return max(arr[0], arr[2], arr[4], arr[5])
# 2, 4를 고르면 0, 1, 3, 5인덱스를 이용해서 조합
    else:
        return max(arr[0], arr[1], arr[3], arr[5])


n = int(input())
dice = []
for _ in range(n):
    dice.append(list(map(int, input().split())))

result = 0
for i in range(6):
    temp = 0
    bottom = dice[0][i]
    
    for j in range(n):
        # 먼저 아랫면의 인덱스를 찾음
        index = 0
        while(index < 6):
            if dice[j][index] == bottom:
                break
            index += 1
        # 옆면의 4개 수 중에서 최댓값을 찾아 temp에 더함
        temp += side_max(index, dice[j])
        # 윗면의 수를 찾아서 bottom을 갱신
        bottom = dice[j][next_index(index)]
    
    if temp > result:
        result = temp


print(result)