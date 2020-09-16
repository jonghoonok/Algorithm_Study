# recursive
def binary_search(arr, start, end, target):
    mid = (start + end)//2
    
    if start > end:
        return None

    if arr[mid] > target:
        binary_search(arr, start, mid-1, target)
    elif arr[mid] < target:
        binary_search(arr, mid+1, end, target)
    else:
        return mid

# repitition
def binary_search2(arr, start, end, target):
    while start <= end:
        mid = (start + end)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None
        