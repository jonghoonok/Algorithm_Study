# import sys

# sys.stdin = open("D3_2806_input.txt", "r")

import copy

def clear(x, y, plate):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    
    for i in range(8):
        new_x = x
        new_y = y
        while True:
            new_x += dx[i]
            new_y += dy[i]
            if 0 <= new_x < n and 0 <= new_y < n and plate[new_y][new_x] != 2:
                plate[new_y][new_x] = 0
            else:
                break
    return plate

# DFS 방식
# 2차원 배열 plate을 매번 deep copy, clear를 통해 퀸이 못 가는 자리를 0으로
# 1이 들어가지 않은 행이 존재하면 불가능한 배열로 0을 리턴
# 마지막 행에 도달했으면 성공한 것이므로 1을 리턴
def chess(index, plate):
    if 1 not in plate[index]:
        return 0
    if index == n-1:
        return 1
    else:
        result = 0
        for i in range(n):
            if plate[index][i]:
                plate[index][i] = 2
                # 단순히 슬라이싱만으로는 리스트 안의 mutable을 카피 불가
                new_plate = clear(i, index, copy.deepcopy(plate))
                result += chess(index+1, new_plate)
                plate[index][i] = 1
            else:
                continue
    return result


# index는 현재 몇 번째 행을 보고 있는지
# col은 각 행에서 퀸이 위치한 가로 인덱스
def chess2(index, col):
    result = 0
    
    # 지금의 퀸 배열이 가능한지 체크하고 아니면 0을 리턴해 되돌아감
    if not promissing(index, col):
        return 0
    if index == n:
        return 1
    else:
        for i in range(1, n+1):
            # 퀸을 하나 놓아보고 재귀함수를 타고 돌아와 해당 경우에 대해 몇 개가 가능한지 result에 더함
            if i in col:
                continue
            col[index+1] = i
            result += chess2(index+1, col)
    return result


def chess3(index, col):
    result = 0    
    if index == n:
        return 1
    else:
        for i in range(1, n+1):
            # 퀸을 하나 놓아보고 재귀함수를 타고 돌아와 해당 경우에 대해 몇 개가 가능한지 result에 더함
            col[index+1] = i
            if promissing(index+1, col):
                result += chess3(index+1, col)
            else:
                continue
    return result


def promissing(i, col):    
    k = 1
    flag = True 
    # 첫째행에서부터 내려오며 i행에 퀸을 놓은 것이 타당한지 체크
    while k < i and flag:
        if col[k] == col[i] or abs(col[k] - col[i]) == (i - k):
            flag = False
            break
        k += 1
    return flag
    

t = int(input())
for test_case in range(t):
    n = int(input())
    chess_plate = [[1]*n for _ in range(n)]
    # col을 0으로 초기화하면 제일 왼쪽에 퀸을 놓을 수 없음(대각선)
    col = [-1]*(n+1)
    # print('#' + str(test_case + 1), chess(0, chess_plate))
    print('#' + str(test_case + 1), chess3(0, col))
