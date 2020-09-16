def quick(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]

    # 역순으로 정렬해야하니 큰 것을 left로
    left = [x for x in tail if x > pivot]
    right = [x for x in tail if x <= pivot]

    return quick(left) + [pivot] + quick(right)


N = int(input())
arr = [int(input()) for _ in range(N)]
print(' '.join(map(str, quick(arr))))