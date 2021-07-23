import sys

def pre_order(arr):

    pre_arr.append(arr[0])       # root를 출력

    if arr[1] != '.':
        pre_order(tree[ord(arr[1]) - ord('A')])  # 왼쪽 서브트리 순회
    if arr[2] != '.':
        pre_order(tree[ord(arr[2]) - ord('A')])  # 오른쪽 서브트리 순회


def in_order(arr):

    if arr[1] != '.':
        in_order(tree[ord(arr[1]) - ord('A')])  # 왼쪽 서브트리 순회
    
    in_arr.append(arr[0])       # root를 출력
    
    if arr[2] != '.':
        in_order(tree[ord(arr[2]) - ord('A')])  # 오른쪽 서브트리 순회


def post_order(arr):

    if arr[1] != '.':
        post_order(tree[ord(arr[1]) - ord('A')])  # 왼쪽 서브트리 순회
    if arr[2] != '.':
        post_order(tree[ord(arr[2]) - ord('A')])  # 오른쪽 서브트리 순회
    
    post_arr.append(arr[0])       # root를 출력


tree = [[] for _ in range(26)]
for i in range(26):
    tree[i].append(chr(ord('A')+i))

n = int(sys.stdin.readline())
for _ in range(n):
    root, l, r = sys.stdin.readline().split()
    tree[ord(root) - ord('A')].append(l)
    tree[ord(root) - ord('A')].append(r)

pre_arr = []
in_arr = []
post_arr = []
pre_order(tree[0])
in_order(tree[0])
post_order(tree[0])

print(''.join(pre_arr))
print(''.join(in_arr))
print(''.join(post_arr))