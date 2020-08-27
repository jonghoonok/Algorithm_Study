import sys

sys.stdin = open("D4_1211_input.txt", "r")

# 1210을 변형: 아래로 내려가는 것으로
def ladder_DFS(matrix, x, y):
    visited = []    
    stack = []
    stack.append([x, y]) 
    cnt = 0             # 경로의 길이

    # DFS
    while stack:
        w = stack.pop()
        # 제일 아래에 도달하면 반복문 탈출
        if w[1] == 99:
            break
        if w not in visited:
            visited.append(w)
            # 아래와 연결되어 있을 경우 스택에 추가
            if matrix[w[1]+1][w[0]]:
                stack.append([w[0], w[1]+1])
            # x좌표가 0 이상이고 w왼쪽에 길이 나 있으며 방문한 적 없으면스택에 추가
            if w[0] > 0 and matrix[w[1]][w[0]-1] == 1 and [w[0]-1, w[1]] not in visited:
                stack.append([w[0]-1, w[1]])
            # x좌표가 99 이하이고 w오른쪽에 길이 나 있으면 방문한 적 없으면 스택에 추가
            if w[0] < 99 and matrix[w[1]][w[0]+1] == 1 and [w[0]+1, w[1]] not in visited:
                stack.append([w[0]+1, w[1]])
        cnt += 1
    return cnt

# 각 출발점에서 DFS를 돌려 경로의 길이가 짧은 x를 저장 후 반환
def min_path(matrix):
    temp = 10000
    result = 0
    for x in range(100):
        if matrix[0][x] == 1:
            path = ladder_DFS(matrix, x, 0)
            if path < temp:
                result = x
                temp = path
    return result

for test_case in range(10):
    n = int(input())
    ladder_list = [list(map(int, input().split())) for _ in range(100)]    
    print('#'+str(test_case+1), min_path(ladder_list))
