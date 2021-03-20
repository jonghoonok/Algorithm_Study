def selection_sort(arr):
    for i in range(len(arr)-1):
        # 배열 내에서 가장 작은 원소를 찾아서 인덱스 i에 저장
        minId = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minId]:
                minId = j
        # 찾았으면 (for문이 끝났으면) 정렬되지 않은 수 중에 제일 앞의 수와 swap
        arr[minId], arr[i] = arr[i], arr[minId]