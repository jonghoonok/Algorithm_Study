import sys

sys.stdin = open("D4_1258_input.txt", "r")

# 화학용기를 만나면 테두리를 따라 돌아 행과 열의 길이를 리턴해주는 함수
def check(x, y, matrix):
    dx = [0, 1] # 시계방향으로 용기를 돌아감
    dy = [1, 0]
    x_cnt = 1
    y_cnt = 1
    new_x = x
    new_y = y
    while new_y + dy[0] < n and matrix[new_x][new_y + dy[0]] != 0:
        new_x += dx[0]
        new_y += dy[0]
        y_cnt += 1
    while new_x + dx[1] < n and matrix[new_x + dx[1]][new_y] != 0:
        new_x += dx[1]
        new_y += dy[1]
        x_cnt += 1
    # 중복을 막기 위해 계산이 끝난 용기에 대해 원소를 모두 0으로 변경
    for i in range(x, x + x_cnt):
        for j in range(y, y + y_cnt):
            matrix[i][j] = 0

    return [x_cnt, y_cnt]

# 테이블을 돌면서 화학용기의 갯수와 크기를 저장하는 함수
def chem(matrix):
    cnt = 0
    result = []
    # 0이면 패스, 숫자를 만나면 용기가 시작되는 지점으로 간주    
    for i in range(n):        
        for j in range(n):
            if matrix[i][j] == 0:            
                pass
            else:
                cnt += 1
                result.append(check(i, j, matrix))                

    # selection sort를 이용해 작은 용기를 앞으로 배치   
    for i in range(cnt-1):
        temp = i
        for j in range(i+1, cnt):
            if result[j][0]*result[j][1] < result[temp][0]*result[temp][1]:
                temp = j
            # 크기가 같으면 행의 길이가 짧은 용기를 앞으로 해 줌
            elif result[j][0] * result[j][1] == result[temp][0] * result[temp][1]:
                if result[j][0] < result[temp][0]:
                    temp = j
        result[i], result[temp] = result[temp], result[i]
    
    # extend를 이용하여 결과물 리턴
    chem_result = [cnt]
    for i in range(cnt):
        chem_result.extend(result[i])
    print(*chem_result)
    

t = int(input())
for test_case in range(t):
    n = int(input())
    chem_list = [list(map(int, input().split())) for _ in range(n)]            
    print('#'+str(test_case+1), end = ' ')
    chem(chem_list)