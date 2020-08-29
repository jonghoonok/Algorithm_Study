import sys

sys.stdin = open("D3_1289_input.txt", "r")


def change_bit(num):
    cnt = 0
    status = '1'
    i = 0
    while i < len(num):
        if num[i] == status:
            cnt += 1
            if status == '1':
                status = '0'
            else:
                status = '1'
        i += 1

    return cnt    


t = int(input())
for test_case in range(t):
    n = input()
    print('#' + str(test_case + 1), change_bit(n))
