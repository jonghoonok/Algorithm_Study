def solution(p):
    if not p:
        return p    
    # 두 균형잡힌 괄호 문자열로 분리
    u = ''
    v = ''
    i = 1
    while i <= len(p):
        temp = p[:i]
        temp2 = p[i:]
        if check_balance(temp) and check_balance(temp2):                       
            u += temp
            v += temp2
            break            
        i += 1
    # 문자열 u가 올바른지 체크
    if check_correct(u):
        # 올바르다면 v에 대해 수행 후 u에 붙여서 반환
        return u + solution(v)
    else:
        # u를 올바르게 해줌
        temp = '(' + solution(v) + ')'            
        temp2 = ''
        for char in u[1:-1]:
            if char == '(':
                temp2 += ')'
            else:
                temp2 += '('
        return temp + temp2                

        
def check_balance(chars):
    cnt_l = 0
    cnt_r = 0
    for char in chars:
        if char == '(':
            cnt_l += 1
        else:
            cnt_r += 1
    if cnt_l == cnt_r:
        return True
    else:
        return False
    
    
def check_correct(chars):
    if len(chars)==0:
        return True
    stack = []
    stack_r = []
    for char in chars:
        stack.append(char)
    for i in range(len(stack)):
        pop = stack.pop()
        if i == 0 and pop == '(':
            return False
        if pop == ')':
            stack_r.append(pop)
        else:
            if stack_r:
                stack_r.pop()
            else:
                return False
    return True


print(solution('()))((()'))