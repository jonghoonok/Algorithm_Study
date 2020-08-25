import sys

sys.stdin = open("D2_4865_input.txt", "r")


def str_check2(str1, str2):
    # 문자열 str1에 포함된 글자들이 str2에 몇개씩 들어있는지 저장할 리스트
    check_list = [0]*len(str1)

    for i in range(len(str2)):
        for j in range(len(str1)):          
            # continue를 이용하여 중복된 항목은 패스
            if str1[j] in str1[:j]:
                continue
            if str2[i] == str1[j]:
                check_list[j] += 1
    # max를 구현하여 check_list내 최댓값을 반환
    result = 0
    for element in check_list:
        if element > result:
            result = element
    return result
                
t = int(input())
for test in range(t):
    str1 = input()  
    str2 = input()
    print('#'+str(test+1), str_check2(str1, str2))