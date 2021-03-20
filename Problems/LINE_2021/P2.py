inp_str = "ZzZz9Z824"

result = []

# 5가지 규칙을 만족하는지 체크하는 리스트
# 위반하면 1 아니면 0
check = [0] * 5

# 1번 규칙 판단
if len(inp_str) > 15 or len(inp_str) < 8:
    check[0] = 1

# 2, 3번 규칙 판단

# 특수 문자 ~!@#$%^&* 의 ASCII 코드는 [126, 33, 64, 35, 36, 37, 94, 38, 42]이다
special = [126, 33, 64, 35, 36, 37, 94, 38, 42]

letter_group = [0]*4
for letter in inp_str:
    asc = ord(letter)
    if 65 <= asc < 91:
        letter_group[0] += 1
    elif 97<= asc < 123:
        letter_group[1] += 1
    elif 48<= asc < 58:
        letter_group[2] += 1
    elif asc in special:
        letter_group[3] += 1

    # 4가지 문자 그룹 모두에 존재하지 않는다: 2번 규칙 판단
    else:
        check[1] = 1

# 3번 규칙 판단
rule_3 = 0
for i in range(4):
    if not letter_group[i]:
        rule_3 += 1
if rule_3 > 1:
    check[2] = 1

# 4번 판단
# 이미 등장했던 문자를 저장하는 배열
existence = [inp_str[0]]
# 연속하는 횟수를 세는 카운터
cnt = 1
for i in range(1, len(inp_str)):
    if inp_str[i] == existence[-1]:
        cnt += 1
        if cnt >= 4:
            check[3] = 1
            break
    else:
        cnt = 1

    existence.append(inp_str[i])


# 5번 판단
inp = set(inp_str)
if len(inp) > len(inp_str) - 4:
    check[4] = 0
else:
    inp_test = list(inp)
    test = [0]*len(inp_test)
    for letter in inp_str:
        for i in range(len(inp)):
            if letter == inp_test[i]:
                test[i] += 1
    for t in test:
        if t >= 5:
            check[4] = 1

# 위반한 규칙들을 반환한다
ans = []
for i in range(5):
    if check[i]:
        ans.append(i+1)
if not ans:
    ans.append(0)
print(ans)