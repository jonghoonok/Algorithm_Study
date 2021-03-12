import sys
sys.setrecursionlimit(10**6)

def dfs(i):
    visit.append(i)
    for j in arr[i]:
        if j not in visit:
            dfs(j)

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
# 인접 행렬과 인접 리스트를 비교했을 때 시간 상 차이는 크지 않음
# 인접 리스트가 메모리 사용이 2배정도 많았음: 동적할당에 사용되는 메모리 큰 걸로 추정
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)

result = 0
visit = []
for i in range(1, n+1):
    # if (1 in arr[i]) and (i not in visit):
    # 자기 자신 외에 연결된 노드가 없어도 자신을 연결하고 있는 연결 그래프로 침 
    if i not in visit:
        result += 1
        dfs(i)

print(result)