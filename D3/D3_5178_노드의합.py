import sys

sys.stdin = open("D3_5178_노드의합_input.txt", "r")


# 반복문을 이용하여 뒤에서부터 채우는 방식
def node_sum(target):
    last = n
    # 2개씩 더하면서 반복하기 위해 n이 홀수인 경우 부모 노드에 값을 적어주고 n-1부터 시작
    if last % 2 == 0:
        Tree[last//2] = Tree[last]
        last -= 1

    for i in range(last, target, -2):        
        Tree[i//2] = Tree[i]+Tree[i-1]
    
    return Tree[target]


# 후위 순회를 이용한 심플한 구현
def post_order(v):
    if v > n:
        return 0
    left = post_order(v*2)
    right = post_order(v*2+1)
    Tree[v] += left + right
    return Tree[v]


t = int(input())
for test_case in range(t):    
    n, m, l = map(int, input().split())
    
    Tree = [0]*(n+1)    
    for _ in range(m):
        num, value = map(int, input().split())
        Tree[num] = value
    
    print('#' + str(test_case + 1), node_sum(l))    
