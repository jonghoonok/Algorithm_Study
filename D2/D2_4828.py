import sys

sys.stdin = open("D2_4828_input.txt", "r")

def counting_sort(nums):
    count_list = [0] * 1000000
    for i in range(len(nums)):
        count_list[nums[i]-1] += 1
    for j in range(len(count_list)):
        count_list[j] += count_list[j-1]
    new_list = [0] * len(nums)
    for j in range(len(nums)-1, 0, -1):
        new_list[count_list[nums[j]] - 1] = nums[j]
        count_list[nums[j]] -= 1
    return new_list

t = int(input())

for test_case in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    new_numbers = counting_sort(numbers)  
    result = new_numbers[n-1] - new_numbers[0]
    print('#'+str(test_case+1), result)