def insertion_sort(arr):
    # 첫 번째 원소는 놔두고 두 번째 원소부터 시작
    for i in range(1, len(arr)):
        # 현재 보고 있는 원소 arr[i]를 앞에 있는 수들과 비교
        for j in range(i, 0, -1):
            # 앞의 수가 더 작다면 swap하여 앞으로 이동, 아니면 stop
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break