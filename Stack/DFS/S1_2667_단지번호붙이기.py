# 백준 2667번
# 단지번호붙이기

import sys

sys.stdin = open("S1_2667_input.txt", "r")


def danji():
    result = []

    for i in range(N):
        for j in range(N):
            if danji_list[i][j]:
                result.append(DFS([j, i]))
    
    result.sort()
    print(len(result))
    for i in range(len(result)):
        print(result[i])


def DFS(v):
    visit = []
    stack = []
    stack.append(v)
    while stack:
        w = stack.pop()
        if w not in visit:
            visit.append(w)
            danji_list[w[1]][w[0]] = 0
            stack.extend(adjacency(w))
    
    return len(visit)


def adjacency(v):
    result = []
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    new_x = v[0]
    new_y = v[1]
    for i in range(4):
        new_x += dx[i]
        new_y += dy[i]
        if 0 <= new_x < N and 0 <= new_y < N and danji_list[new_y][new_x]:
            result.append([new_x, new_y])
        new_x = v[0]
        new_y = v[1]
    return result


N = int(input())
danji_list = []
for _ in range(N):
    danji_list.append(list(map(int, input())))
danji()