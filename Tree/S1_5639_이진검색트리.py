import sys
sys.setrecursionlimit(100000)

# 후위 순회한 결과를 출력하는 함수
def post_order(tree):
    # 탈출조건 : 트리 말단
    if not tree:
        return

    post_order(tree[1]) # left child 방문
    post_order(tree[2]) # right child 방문
    print(tree[0])      # root를 출력


# 전위 순회한 결과 배열을 트리로 변환하는 함수
def pre_order_to_tree(arr):
    if not arr:
        return []
    if len(arr) == 1:
        return [arr[0], [], []]
    
    tree = []

    # root 추가
    tree.append(arr[0])

    # root값 기준으로 왼쪽 서브트리와 오른쪽 서브트리를 구분
    # 편향되어있을 수 있으니 투 포인터를 이용
    i, n = 1, len(arr)
    j = n-1
    while i < n or j > 1:
        if arr[i] > arr[0]:
            # 왼쪽 서브트리 추가
            tree.append(pre_order_to_tree(arr[1:i]))
            # 오른쪽 서브트리 추가
            tree.append(pre_order_to_tree(arr[i:]))
            break
        if arr[j] < arr[0]:
            # 왼쪽 서브트리 추가
            tree.append(pre_order_to_tree(arr[1:j+1]))
            # 오른쪽 서브트리 추가
            tree.append(pre_order_to_tree(arr[j+1:]))
            break
        i += 1
        j -= 1

    return tree


# 트리 작성 없이 바로 후위 순회로 출력
def pre_to_post(start, end):
    if start > end:
        return

    # root를 기준으로 서브트리를 나눔
    # 편향되어있을 수 있으니 투 포인터를 이용
    l, r = start+1, end
    while l <= end:
        if array[l] > array[start]:
            pre_to_post(start+1, l-1)
            pre_to_post(l, end)
            break
        if array[r] < array[start]:
            pre_to_post(start+1, r)
            pre_to_post(r+1, end)
            break
        l += 1
        r -= 1

    print(array[start])


array = []
# 반복문?
while True:
    try:
        num = int(input())
        array.append(num)
    except:
        break

pre_to_post(array)
# post_order(pre_order_to_tree(array))