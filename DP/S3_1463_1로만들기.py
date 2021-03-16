n = int(input())
# 연산을 최소한으로 사용하여 1이 될 수 있는 횟수를 담은 배열
arr = [0]*(n+1)

arr[1] = 0
i = 2
while i < n+1:
    arr[i] = arr[i-1] + 1
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i//2]+1)
    # elif를 이용하면 누락하는 경우가 생길 수 있음
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i//3]+1)
    i += 1

print(arr[n])