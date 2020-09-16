def binary_search(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


N = int(input())
elements = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

elements.sort()
for target in targets:
    if binary_search(elements, 0, N-1, target):
        print('yes')
    else:
        print('no')