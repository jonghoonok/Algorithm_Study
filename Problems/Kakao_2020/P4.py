def solution(n, s, a, b, fares):
    # FloydWarshall 알고리즘 사용
    INF = int(1e9)
    graph = [[INF]*(n) for _ in range(n)]

    # 자기 자신으로 가는 거리는 0으로 초기화
    for i in range(n):                   
        graph[i][i] = 0

    # 노드 c에서 d로 가는 거리 f를 입력받아 그래프 작성
    for fare in fares:
        c, d, f = fare[0]-1, fare[1]-1, fare[2]
        graph[c][d] = f
        graph[d][c] = f

    # 점화식에 따라 각 노드 k에 대해 c에서 d로 가는 최단거리 갱신
    # c-d로 직접가는 것보다 c-k-d로 가는 거리가 짧으면 갱신
    for k in range(n):
        for c in range(n):
            for d in range(n):                
                if graph[c][d] > graph[c][k]+graph[k][d]:
                    graph[c][d] = graph[c][k]+graph[k][d]

    # a와 b가 k까지 같이가고 그 후에 각자 갈 때 비용의 합
    cost = INF
    for k in range(n):
        cost_temp = graph[s-1][k] + graph[k][a-1] + graph[k][b-1]
        if cost_temp < cost:
            cost = cost_temp

    return cost

input1 = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(6, 4, 6, 2, input1))

input2 = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
print(solution(7, 3, 4, 1, input2))

input3 = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
print(solution(6, 4, 5, 6, input3))