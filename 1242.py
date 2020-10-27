import sys

sys.stdin = open("1242_input.txt", "r")


def password_check(numbers):
    # 16진수코드를 저장하는 리스트
    code_list = []

    # 배열을 돌면서 암호코드 찾기
    for i in range(n):
        temp = ''
        x = 0
        for j in range(m):
            # 0이 아닌 수가 나오면 temp로 전부 더한 후 뒤에 0을 다 빼기
            if numbers[i][j] != '0':
                temp = ''.join(numbers[i][j:])
                x = j
                break

        # 찾았으면 뒤의 0 빼고 리스트에 담고 암호코드 있는자리 다 0으로
        if temp:
            for j in range(len(temp)-1, 0, -1):
                if temp[j] != '0':
                    temp = temp[:j+1]
                    break
            code_list.append(temp)
            y = i
            while numbers[y][x] != '0':
                y += 1
            for k in range(i, y):
                for l in range(x, x+len(temp)):
                    numbers[k][l] = '0'
    
    # 이진코드로 변환
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
    bin_list = []
    for code in code_list:
        temp = ''
        l = len(code)
        for i in range(l):
            # 마지막에 뒤에 붙은 0 떼기
            if i == l-1:
                if code[i] in ['2', '6', 'A', 'E']:
                    temp += table[code[i]][:3]        
                    break
                elif code[i] in ['4', 'C']:
                    temp += table[code[i]][:2]        
                    break
                elif code[i] == '8':
                    temp += table[code[i]][:1]        
                    break
            temp += table[code[i]]

        # 이진코드의 길이를 56으로 조정
        l = len(temp)
        remainder = l % 56
        # 앞에 있는 0 떼거나 붙이기
        if remainder != 0:
            if remainder < 3:
                temp = temp[remainder:]
            else:
                temp = '0'*(56-remainder) + temp
        # 길이가 56n이면 56으로 만들기
        l = len(temp)
        quotient = l // 56
        if quotient > 1:
            temp_temp = ''
            for i in range(l//quotient):
                temp_temp += temp[i*quotient]
            temp = temp_temp

        bin_list.append(temp)
    
    # 숫자로 변환
    num_list=['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
    # 변환된 결과를 담는 리스트
    result_list = []

    i = 0
    for code in bin_list:
        temp = [0]*8
        for i in range(8):
            temp[i] = num_list.index(code[i*7:i*7+7])

        result_list.append(temp)

    # 검증코드가 맞는지 확인하고 result에 더함
    result = 0    
    for code in result_list:
        temp = 0
        for j in range(8):
            if j % 2 == 0:
                temp += 3*code[j]
            else:
                temp += code[j]
        if temp % 10 == 0:
            result += sum(code)

    return result            


t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    numbers = [list(input()) for _ in range(n)]    
    print('#' + str(test_case + 1), password_check(numbers))