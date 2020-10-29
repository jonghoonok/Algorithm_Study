import sys

sys.stdin = open("D3_5189_전자키트_input.txt", "r")


# 가지치기 없는 버전
# arr에는 1을 제외한 사무실들의 순열을 저장
def kit(arr, n, k):
    if k == n:
        # 먼저 1부터 arr[0] 사무실까지의 소비량
        result = num_list[0][arr[0]-1]
        # arr 순서대로 이동할 때 배터리 소비량
        for i in range(n-1):
            result += num_list[arr[i]-1][arr[i+1]-1]
        # 다시 1로 돌아올 때 소비량
        result += num_list[arr[-1]-1][0]        
        return result
    else:        
        result = int(1e9)
        # 반복문을 돌며 가장 작은 소비량을 리턴
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            temp = kit(arr, n, k+1)
            arr[k], arr[i] = arr[i], arr[k]
            if temp < result:
                result = temp
        return result


t = int(input())
for test_case in range(t):
    n = int(input())
    num_list = [list(map(int, input().split())) for _ in range(n)]
    arr = [i+1 for i in range(1,n)]
    print('#' + str(test_case + 1), kit(arr, n-1, 0))