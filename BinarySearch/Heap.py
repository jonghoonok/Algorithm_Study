# minHeap
def heappush(value):
    global heapcnt
    heapcnt += 1
    heap[heapcnt] = value
    cur = heapcnt
    parent = cur // 2
    # 루트가 아니고, 부모노드의 값이 자식노드보다 크면 swap
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2


def heappop():
    global heapcnt
    retValue = heap[1]
    heap[1] = heap[heapcnt]
    heap[heapcnt] = 0
    heapcnt -= 1

    parent = 1
    child = parent * 2

    if child + 1 <= heapcnt:    # 오른쪽 자식 존재
        if heap[child] > heap[child+1]:
            child += 1
    # 자식노드가 존재하고, 부모노드의 값이 자식노드보다 크면 swap
    while child <= heapcnt and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heapcnt:    
            if heap[child] > heap[child+1]:
                child += 1
    
    return retValue


heapcnt = 0
temp = [7, 2, 5, 3, 4, 6]
n = len(temp)
heap = [0]*(n+1)
for i in range(n):
    heappush(temp[i])

for i in range(n):
    print(heappop(), end=" ")
print()