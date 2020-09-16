# C style
def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if arr[left] <= arr[pivot]:
            left += 1
        if arr[right] > arr[pivot]:
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
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

    quick_sort_py(left) + [pivot] + quick_sort_py(right)
