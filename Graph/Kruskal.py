from collections import defaultdict
from heapq import *

from DisjointSets import find_root, union_parent
import sys


# 간선들을 비용 오름차순으로 정렬한 뒤 하나씩 사이클을 검사해 추가
# Disjoint를 이용
def mst1():
    cnt = 0
    total_cost = 0

    for i in range(E):
        px = find_root(edge[i][0])
        py = find_root(edge[i][1])

        # cycle check
        if px != py:
            total_cost += edge[i][2]
            cnt += 1
            union(px, py)
            # root[py] = px
        
        # MST의 간선의 수는 노드의 개수 -1 이다
        if cnt == V-1:
            break
    
    return total_cost


# 집합 자료구조를 이용해 현재 트리에 없는 노드만 추가하기 때문에 사이클이 발생하지 않음 
def mst2():
    tree = set([1])  # 현재 만들어진 트리
    
    edges = graph[1]  # 방문할 간선 리스트: 최소 힙을 이용하여 가장 적은 비용의 간선을 pop함
    heapify(edges)
    
    total_cost = 0  # MST의 가중치
    
    while edges:
        weight, node = heappop(edges)
        
        if node not in tree:
            tree.add(node)
            total_cost += weight
            
            for edge in graph[node]:
                if edge[1] not in tree:
                    heappush(edges, edge)

    return total_cost


# mst1에 사용할 입력
V, E = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(E)]
edge.sort(key=lambda x: x[2])
# root 노드를 저장하는 배열
root = [0] * V

for i in range(V):
    root[i] = i

# mst2에 사용할 그래프
# graph = defaultdict(list)
# for i in range(E):
#     A, B, C = map(int, sys.stdin.readline().split())
#     graph[A].append((C, B))  # 비용, 인접 노드
#     graph[B].append((C, A))

print(mst1())
# print(mst2())