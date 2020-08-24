import sys

sys.stdin = open("D3_1221_input.txt", "r")

# 풀이1: 문자열의 값을 하나씩 따져 선택 정렬을 이용하여 정렬하기
# pass하긴 하지만 시간이 너무 오래 걸림
# def space_sort(numbers):    
#     check = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
#     for i in range(n-1):
#         index = i
#         least = check.index(numbers[i])
#         for j in range(i+1, n):
#             if least > check.index(numbers[j]):
#                 index = j
#                 least = check.index(numbers[j])
#         numbers[i], numbers[index] = numbers[index], numbers[i]
#     print(*numbers)

# 풀이2: 숫자로 변환하고 정렬한 뒤 다시 문자로 변환
def space_sort2(numbers):
    result = []
    num_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    for i in range(n):        
        result.append(num_list.index(numbers[i]))

    # 마찬가지로 선택정렬을 쓰지만 풀이1보다는 훨씬 빠름
    for i in range(n-1):
        least = i        
        for j in range(i+1, n):
            if result[j] < result[least]:
                least = j                
        result[i], result[least] = result[least], result[i]     
    
    new_result=[]
    for i in range(n):
        new_result.append(num_list[result[i]])
    print(*new_result)

t = int(input())
for test_case in range(t):
    test, n = input().split()
    n = int(n)
    space_number = list(input().split())
    print('#' + str(test_case + 1))
    space_sort2(space_number)
