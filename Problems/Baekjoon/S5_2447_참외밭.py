k = int(input())
boundary = [list(map(int, input().split())) for _ in range(6)]

# 작은 변 두개를 찾기: 중복된 방향을 찾으면 된다
small_1, small_2 = 0, 0     # 작은 변 두 개의 길이
big_1, big_2 = 0, 0         # 큰 변 두 개의 길이
check = []               # 각 변의 방향을 담는 배열

for i in range(6):
    if boundary[i][0] in check: # 중복이 검출됨
        # 중복을 검출한 시점은 2개로 분류 가능: 
        # 중복된 변이 한 쌍씩 떨어져 있는 경우
        if i == 4 and boundary[1][1] + boundary[5][1] == boundary[3][1]:
            small_1 = boundary[0][1]
            small_2 = boundary[5][1]
            big_1 = boundary[2][1]
            big_2 = boundary[3][1]
        
        # 중복된 변들이 3개 이상 붙어 있는 경우: 3개가 뒤에 오는 경우
        elif i == 4 and boundary[0][1] + boundary[4][1] == boundary[2][1]:
            small_1 = boundary[4][1]
            small_2 = boundary[5][1]    
            big_1 = boundary[1][1]
            big_2 = boundary[2][1]
        
        # 중복된 변들이 3개 이상 붙어 있는 경우: 3개가 앞에 오는 경우
        elif i == 2 and boundary[1][1] + boundary[5][1] == boundary[3][1]:
            small_1 = boundary[0][1]
            small_2 = boundary[1][1]    
            big_1 = boundary[3][1]
            big_2 = boundary[4][1]
        
        # 중복된 변들이 3개 이상 붙어 있는 경우: 4개가 한번에 오는 경우
        else:
            small_1 = boundary[i][1]
            small_2 = boundary[i-1][1] 
            big_1 = boundary[i-2][1] + boundary[i][1]
            big_2 = boundary[i-1][1] + boundary[i+1][1]
        break

    else:
        check.append(boundary[i][0])


# 큰 사각형에서 작은 사각형 넓이를 찾기
print(k*(big_1*big_2-small_1*small_2))