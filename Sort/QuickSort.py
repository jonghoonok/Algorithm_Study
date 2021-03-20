# C style
def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을때까지
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을때까지
        while right > start and arr[right] > arr[pivot]:
            right -= 1
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        # 최소한 left 왼쪽으로는 전부 피벗보다 작음이 보장되기 때문
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)


# python style
def quick_sort_py(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort_py(left) + [pivot] + quick_sort_py(right)
