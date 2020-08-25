import sys

sys.stdin = open("D2_4864_input.txt", "r")


# def str_check(pattern, target):
#     i = 0
#     j = 0
#     # 브루트포스를 이용하여 체크
#     while j < len(target):        
#         if pattern[i] != target[j]:
#             j = j-i
#             i = -1            
#         i += 1
#         j += 1
#         if i == len(pattern):
#             return 1
#     return 0

# KMP Algorithm
def str_check2(pattern, target):
    # lps 구하기
    PI = [0]*len(pattern)
    j = 0    
    for i in range(1, len(pattern)):
        
        while j > 0 and pattern[i] != pattern[j]:
            j = PI[j-1]

        if pattern[i] == pattern[j]:
            j += 1
            PI[i] = j
             
    # kmp
    j = 0
    for i in range(len(target)):
        
        while j > 0 and target[i] != pattern[j]:
            j = PI[j-1]

        if target[i] == pattern[j]:
            if j == len(pattern) -1:
                return 1
            j += 1        
    
    return 0
                
t = int(input())
for test in range(t):
    str1 = input()  
    str2 = input()
    print('#'+str(test+1), str_check2(str1, str2))