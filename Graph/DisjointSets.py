# 공통 원소가 없는 두 집합
# 각 집합은 root node로 구분됨
def find_parents(parent, x):
    if parent[x] != x:
        return find_parents(parent, parent[x])
    return x
    # # path compression
    # if parent[x] != x:
    #     parent[x] = find_parents(parent, parent[x])
    # return parent[x]

def union_parent(parent, a, b):
    a = find_parents(parent, a)
    b = find_parents(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0]*(v+1)

# 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end=" ")
for i in range(1, v+1):    
    print(find_parents(parent, i), end=" ")
print()


print(' '.join(map(str, parent)))

# Cycle 찾기: 모든 간선에 대해 find와 union을 반복
# 부모 테이블 초기화(#21) 이후 시작
cycle = False
for i in range(e):
    a, b = map(int, input().split())
    if find_parents(parent, a) == find_parents(parent, b):
        cycle = True
    else:
        union_parent(parent, a, b)
