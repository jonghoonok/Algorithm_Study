# Pseudo
# def perm(n, k):
#     if k == n:
#         print array
#     else:
#         for i in range(k, n):
#             swap(k, i)      # arr[k], arr[i] 교환
#             perm(n, k+1)    # n: 원소의 갯수, k: 현재까지 교환된 원소의 갯수
#             swap(k, i)      # 리턴할 때 원래 자리로 되돌려놔야 함

# perm(3, 0)으로 돌려보면
# [1, 2, 3]으로 시작
# swap(0, 0) -> [1, 2, 3]
# perm(3, 1)
# swap(1, 1) -> [1, 2, 3]
# perm(3, 2)
# swap(2, 2) -> [1, 2, 3]
# perm(3, 3)
# print [1, 2, 3]
# swap(2, 2) -> [1, 2, 3]

# swap(1, 1) -> [1, 2, 3]
# swap(1, 2) -> [1, 3, 2]
# perm(3, 2)
# swap(2, 2) -> [1, 3, 2]
# print [1, 3, 2]
# swap(2, 2) -> [1, 3, 2]

# 이런식으로 계속 이어진다. 그림으로 그리는 것이 더 이해하기 쉬움


# Code
def permutation(n, k):
    if k == n:
        print(arr)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            permutation(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]


n = 3
arr = [i+1 for i in range(n)]
permutation(n, 0)