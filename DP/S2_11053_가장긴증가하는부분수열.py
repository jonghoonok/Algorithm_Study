def binary(arr, start, end, target):
    if start > end:
        return start

    mid = (start + end) // 2
    if target > arr[mid][1]:
        return binary(arr, mid+1, end, target)
    elif target < arr[mid][1]:
        return binary(arr, start, mid-1, target)
    else:
        return mid


# 풀이1: O(N^2)
def LIS1():
    # nums[i]를 마지막 원소로 하는 '증가하는 순열'의 길이를 담는 배열
    LIS = [0]*n
    for i in range(n):
        # nums[i]보다 작은 수 중에, 증가하는 순열의 길이를 최대가 되게 하는 인덱스j를 찾음
        temp = 0
        for j in range(i):
            if nums[j] < nums[i] and LIS[j] > temp:
                temp = LIS[j]
        LIS[i] = temp + 1

    # LIS배열 내에서 최댓값을 출력하면 종료
    print(max(LIS))


# 풀이2: O(NlogN)
def LIS2():
    # nums[i]보다 작은 nums[j]들 중에 최대의 LIS[j]를 갖는 j를 찾음
    # 단, 순차적으로 탐색하는 것이 아니라 이진탐색을 하기 위해 새로운 배열을 작성
    LIS = [[1, nums[0]]]    # 첫 번째 인덱스는 LIS 길이, 두 번째 인덱스는 해당 LIS의 마지막 수가 될 수 있는 수 중에서 가장 작은 수
    for i in range(1, n):
        # nums[i]가 LIS에서 몇 번 째 위치로 갈 수 있는지 탐색  
        index = binary(LIS, 0, len(LIS)-1, nums[i])
        if index > len(LIS)-1:
            LIS.append([LIS[-1][0]+1, nums[i]])
        else:
            LIS[index] = [LIS[index][0], nums[i]]

    # LIS배열 내에서 최댓값을 출력하면 종료
    print(LIS[-1][0])


n = int(input())
nums = list(map(int, input().split()))

# LIS1()
LIS2()
