# 내 풀이: 잘못됨
def reorderLogFiles_1(self, logs: List[str]) -> List[str]:
    dig = []
    let = []
    for log in logs:
        for i in range(100):
            if log[i] != ' ':
                continue
            if ord(log[i+1]) in range(48, 58):
                dig.append(log)
            else:
                let.append(log[i+1:] + " " + log[:i])
            break

    # 여기서 잘못됨: 앞의 식별자가 문자보다 알파벳이 빠르다면 식별자 기준으로 정렬되어버림
    # 예를 들어 "let1 art zero can"가 "let3 art zero"보다 길기 때문에 뒤에 와야 하나 can이 let보다 빨라 앞에 옴
    let.sort()

    new_let = []
    for log in let:
        for i in range(-2, -100, -1):
            if log[i] == " ":
                log = log[i+1:]+" "+log[:i]
                new_let.append(log)
                break

    return new_let+dig


# split()을 활용하고, 람다를 이용하여 우선순위 정렬 도입
def reorderLogFiles_2(self, logs: List[str]) -> List[str]:
    dig = []
    let = []
    for log in logs:
        if log.split()[1].isdigit():
            dig.append(log)
        else:
            let.append(log)
    
    # 우선순위 정렬: 먼저 식별자를 제외한 것 기준으로 하고 동일하면 식별자 이용
    let.sort(key=lambda x:(x.split()[1:], x.split()[0]))

    return let+dig