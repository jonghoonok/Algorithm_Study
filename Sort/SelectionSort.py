def selection_sort(arr):
    for i in range(len(arr)-1):
        minId = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minId]:
                minId = j
        arr[minId], arr[i] = arr[i], arr[minId]