import sys

sys.stdin = open("D3_1240_input.txt", "r")


def password_check(numbers):
    # 먼저 암호문에 해당되지 않는 행 제거
    i = 0
    while True:
        if not '1' in numbers[i]:
            numbers.pop(i)
        else:
            i += 1
        if len(numbers) == i:
            break

    # 열 제거
    for j in range(m-1, 56, -1):
        if numbers[0][j] == '0':
            continue
        else:
            for k in range(len(numbers)):
                numbers[k] = numbers[k][j-55:j+1]
            break
    
    # 암호코드로 변환
    check_list=['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
    code = [0]*8
    i = 0
    while i < 7:
        code[i] = check_list.index(numbers[0][i*7:i*7+7])
        i += 1
    code[7] = check_list.index(numbers[0][49:])

    # 검증코드가 맞는지 확인
    result = 0
    for j in range(8):
        if j % 2 == 0:
            result += 3*code[j]
        else:
            result += code[j]
    if result % 10 == 0:
        return sum(code)
    else:
        return 0


t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    numbers = [input() for _ in range(n)]    
    print('#' + str(test_case + 1), password_check(numbers))
