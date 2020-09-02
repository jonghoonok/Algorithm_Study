import sys

sys.stdin = open("D4_1210_input.txt", "r")


# 먼저 반복문을 이용하여 구현
def ladder_test(matrix, x, y):        
    move = 0    # 0: up, 1: right, 2, left
    dx = [0, 1, -1]
    dy = [-1, 0, 0]    
    while y > 0:        
        # 우선 move의 값에 따라 이동
        x += dx[move]
        y += dy[move]
        # 이동한 후 주변 환경에 따라 move의 값 변경
        if move == 0:
            if x > 0 and matrix[y][x-1]:    # 왼쪽으로 이동
                move = 2
            if x < 99 and matrix[y][x+1]:   # 오른쪽으로 이동
                move = 1                      
        # 가로방향 이동 중에는 세로 사다리가 나올 때만 변경하고 계속 이동
        elif move == 1:
            if matrix[y-1][x]:
                move = 0
        else:
            if matrix[y-1][x]:
                move = 0
    return x


# 조금 더 DFS스럽게 구현함
def ladder_DFS(matrix, x, y):
    visited = []    
    stack = []
    stack.append([x, y]) 

    # DFS
    while stack:
        w = stack.pop()
        # 제일 위에 도달하면 x좌표를 반환
        if w[1] == 0:
            return w[0]
        if w not in visited:
            visited.append(w)
            # 위와 연결되어 있을 경우 스택에 추가
            if matrix[w[1]-1][w[0]]:
                stack.append([w[0], w[1]-1])
            # x좌표가 0 이상이고 w왼쪽에 길이 나 있으며 방문한 적 없으면스택에 추가
            if w[0] > 0 and matrix[w[1]][w[0]-1] == 1 and [w[0]-1, w[1]] not in visited:
                stack.append([w[0]-1, w[1]])
            # x좌표가 99 이하이고 w오른쪽에 길이 나 있으면 방문한 적 없으면 스택에 추가
            if w[0] < 99 and matrix[w[1]][w[0]+1] == 1 and [w[0]+1, w[1]] not in visited:
                stack.append([w[0]+1, w[1]])


# 체크 함수를 이용하여 재귀적으로 구현
def check(x, y):
    if x<0 or x>99 or y<0 or y>99:
        return False
    if ladder_list[y][x] == 0:
        return False
    return True


def ladder_recursive(x, y):
    if y == 0:
        return x
    else:
        ladder_list[y][x] = 0       # 가는 길을 전부 0으로 바꿔줌
        if check(x, y-1):
            ladder_recursive(x-1, y)
        elif check(x+1, y):
            ladder_recursive(x+1, y)
        else:            
            ladder_recursive(x, y-1)
        ladder_list[y][x] = 1       # 돌아오면서 다시 1로 만들어줌

for test_case in range(10):
    n = int(input())
    ladder_list = [list(map(int, input().split())) for _ in range(100)]
    x = ladder_list[99].index(2)
    y = 99
    print('#'+str(test_case+1), ladder_DFS(ladder_list, x, y))