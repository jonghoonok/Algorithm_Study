import sys
sys.setrecursionlimit(10**6)

def quick_sort_py(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x < pivot]
    right = [x for x in tail if x >= pivot]

    return quick_sort_py(left) + [pivot] + quick_sort_py(right)


def quick_sort_C(arr, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[pivot] >= arr[left]:
            left += 1
        while right > start and arr[pivot] <= arr[right]:
            right -= 1
        if left > right:
            arr[pivot], arr[left] = arr[left], arr[pivot]
        else:
            arr[right], arr[left] = arr[left], arr[right]

    quick_sort_C(arr, start, right - 1)
    quick_sort_C(arr, right + 1, end)


n = int(sys.stdin.readline())
arr = [0]*n
for i in range(n):
    arr[i] = int(sys.stdin.readline())

# ans = quick_sort_py(arr)

quick_sort_C(arr, 0, n-1)

for num in ans:
    print(num)