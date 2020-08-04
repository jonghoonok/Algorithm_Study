import sys

sys.stdin = open("D2_4835_input.txt", "r")

def prefixSum(n, m, nums):
    # N이 100 이하, nums내 원소의 크기가 10000이하이므로 min초기값을 그 곱인 백만으로 설정해야
    max_sum = 0
    min_sum = 1000000
    for i in range(n-m+1):
        prefixsum = 0
        for j in range(m):
            prefixsum += nums[i+j]
        if max_sum < prefixsum:
            max_sum = prefixsum
        if min_sum > prefixsum:
            min_sum = prefixsum

    return max_sum - min_sum

t = int(input())

for test_case in range(t):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    print('#'+str(test_case+1), prefixSum(N, M, numbers))