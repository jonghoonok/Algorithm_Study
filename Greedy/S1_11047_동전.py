# target보다 작거나 같은 최대의 인덱스를 반환함
def binary_search(arr, start, end, target):
    if start > end:
        return start - 1

    mid = (start + end) // 2
    if target > arr[mid]:
        return binary_search(arr, mid+1, end, target)
    elif target < arr[mid]:
        return binary_search(arr, start, mid-1, target)
    else:
        return mid

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

result = 0
# 이진탐색을 수행하여 k보다 작거나 같은 최대 크기의 동전을 찾음
while k:
    biggest_coin = coins[binary_search(coins, 0, n-1, k)]     # 찾은 동전의 크기
    temp = k // biggest_coin                                # 해당 동전으로 k 내에서 최대한을 지불함
    k -= temp * biggest_coin
    result += temp

print(result)