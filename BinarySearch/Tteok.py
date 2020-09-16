def max_cut(arr, start, end, target):
    while start <= end:
        mid = (start+end)//2        
        
        temp = 0
        for i in range(N-1, mid, -1):
            temp += arr[i] - arr[mid]
        
        if temp < target:
            end = mid - 1
        # temp==target이 된다는 보장이 없음
        # result를 설정하여 이것이 최대한 target과 가까워진 후 while문이 끝나면 리턴
        else:
            result = arr[mid]
            start = mid + 1
    return result    


N, M = map(int, input().split())
tteok_list = list(map(int, input().split()))
tteok_list.sort()
print(max_cut(tteok_list, 0, N-1, M))