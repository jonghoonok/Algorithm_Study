program = "line"
flag_rules = ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"]
commands = ["line -n 100 -s hi -e", "line -n 100 -e -num 150"]

# flag name에 따른 argument type을 저장하는 해시 테이블과 alias 관계를 담는 해시테이블 작성
flags = dict()
alias = dict()
for i in range(len(flag_rules)):
    # 현재 보고 있는 flag rule을 공백 기준으로 분리해서 temp에 저장
    temp = list(flag_rules[i].split())
    # temp의 길이가 2면 바로 추가하고, 3이면 ALIAS를 처리함
    if len(temp) == 2:
        # flag name이 key, argument type이 value
        flags[temp[0]] = temp[1]
    else:
        # flag_name1을 key로 하여 flag_name2의 value와 같도록 저장
        flags[temp[0]] = flags[temp[2]]
        # alias 관계도 작성
        alias[temp[0]] = temp[2]
        alias[temp[2]] = temp[0]


answer = [True]*len(commands)

# 각각의 커맨드가 flag rule를 준수하는지 검사
for i in range(len(commands)):
    # 현재 보고 있는 커맨드를 공백 기준으로 분리해서 temp에 저장
    temp = list(commands[i].split())

    # 프로그램 이름이 맞는지 check
    if temp[0] != program:
        # 프로그램 이름이 일치하지 않으면 뒤의 argument 검사 불필요
        # answer에 False를 기입하고다음 커맨드 검사로 넘어감
        answer[i] = False
        continue
    
    # 프로그램 이름 이후의 flag와 argument들을 검사
    j = 1

    # alias 관계인 flag_name이 사용되었는지 나타내는 배열
    alias_check = [0]*len(flag_rules)
    while (j < len(temp)):
        # 먼저 flag name으로 부터 argument type이 string, number, null 중 무엇인지 확인
        try:
            argument_type = flags[temp[j]]
        except KeyError:
            # Key Error가 발생: 현재 보고 있는 커맨드의 flag name이 타당하지 않으니 False 처리하고 다음 커맨드 진행
            answer[i] = False
            break
        
        # 각 argument의 타입에 맞는 커맨드가 입력되었는지 확인
        j += 1
        if argument_type in ("STRING", "STRINGS"):            
            # 다음 flag_name을 만나거나 커맨드의 끝을 만날 때까지 STRING이 맞는지 확인을 반복
            cnt = 0     # 다음 flag name을 만날 때까지 검사하는 argument의 갯수
            while True:
                # 커맨드가 끝났는지 check
                if j >= len(temp):
                    break
                # 다음 flag name을 만났는지 check
                if temp[j][0] == '-':
                    break
               
                cnt += 1
                # 알파벳 대소문자가 아닌 것이 포함되어 있는지 검사
                check = True
                for letter in temp[j]:
                    asc = ord(letter)
                    if (asc not in range(65, 91)) and (asc not in range(97, 123)):
                        check = False
                        break
                j += 1
            
            # type이 STRING인지 STRINGS인지에 따라 다르게 처리
            if argument_type == "STRING":
                # argument가 하나도 없거나(cnt가 0), 여러개를 처리했거나(cnt > 1) STRING이 아닌 것이 들어있었다면(check가 False) answer에 False를 기입하고 현재 커맨드의 검사를 종료
                if cnt != 1 or not check:
                    answer[i] = False
                    break
            else:
                # argument가 하나도 없거나(cnt가 0), STRING이 아닌 것이 들어있었다면(check가 False) answer에 False를 기입하고 현재 커맨드의 검사를 종료
                if not cnt or not check:
                    answer[i] = False
                    break

        elif argument_type in ("NUMBER", "NUMBERS"):
            # 다음 flag_name을 만나거나 커맨드의 끝을 만날 때까지 NUMBER가 맞는지 확인을 반복
            cnt = 0     # 다음 flag name을 만날 때까지 검사하는 argument의 갯수
            while True:
                # 커맨드가 끝났는지 check
                if j >= len(temp):
                    break
                # 다음 flag name을 만났는지 check
                if temp[j][0] == '-':
                    break
               
                cnt += 1
                # 숫자가 포함되어 있는지 검사
                check = True
                try:
                    int(temp[j])
                except:
                    # 예외가 발생했으면 잘못된 인자가 들어온 것이므로 종료
                    check = False
                    break
                
                j += 1
            
            # type이 NUMBER인지 NUMBERS인지에 따라 다르게 처리
            if argument_type == "NUMBER":
                # argument가 하나도 없거나(cnt가 0), 여러개를 처리했거나(cnt > 1) NUMBER가 아닌 것이 들어있었다면(check가 False) answer에 False를 기입하고 현재 커맨드의 검사를 종료
                if cnt != 1 or not check:
                    answer[i] = False
                    break
            else:
                # argument가 하나도 없거나(cnt가 0), NUMBER가 아닌 것이 들어있었다면(check가 False) answer에 False를 기입하고 현재 커맨드의 검사를 종료
                if not cnt or not check:
                    answer[i] = False
                    break
            
        else:
            # NULL이면 argument가 없으므로 다음으로 넘어감
            pass

print(answer)