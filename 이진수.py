import sys

sys.stdin = open("5185_input.txt", "r")


def hex_bin(num):
    table = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }
    
    result = ''
    for i in range(n):
        result += table[num[i]]
    
    return result


t = int(input())
for test_case in range(t):
    n, m = input().split()
    n = int(n)
    print('#' + str(test_case + 1), hex_bin(m))