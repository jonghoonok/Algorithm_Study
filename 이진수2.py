import sys

sys.stdin = open("5186_input.txt", "r")


def deci_bin(num):   
    
    result = ''
    
    for _ in range(12):
        num *= 2
        if num >= 10**(len(n)-2):
            result += '1'
            num -= 10**(len(n)-2)
        else:
            result += '0'
        
        if num == 0:
            return result
    
    return 'overflow'


t = int(input())
for test_case in range(t):
    n = input()
    num = int(n[2:])
    print('#' + str(test_case + 1), deci_bin(num))