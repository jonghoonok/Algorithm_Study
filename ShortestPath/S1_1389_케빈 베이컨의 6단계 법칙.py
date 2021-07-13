import sys

# 각 유저의 케빈-베이컨 수를 계산
def kevin():
    # 플로이드-워셜 알고리즘으로 모든 유저 간의 최단 거리(케빈-베이컨 수)를 계산
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) 


# 가장 적은 케빈 베이컨 수를 갖는 사람의 번호를 리턴
def min_kevin():
    max_kevin = int(1e9)
    result = 1

    for i in range(1, n+1):
        temp = sum(graph[i][1:])
        if temp < max_kevin:
            max_kevin = temp
            result = i

    return result


input = sys.stdin.readline
n, m = map(int, input().split())

# 친구 관계를 나타내는 인접행렬 작성
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i][j], graph[j][i] = 1, 1

kevin()

print(min_kevin())