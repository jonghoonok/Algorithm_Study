import sys

sys.stdin = open("D2_4873_input.txt", "r")


# str이 iteration임을 이용한 방법
def erase(letters):    
    # 중복을 모두 제거할 때까지 반복
    while True:                
        original_letters = letters
        for j in range(len(letters)-1):
            # 중복이 발견되면 두 글자를 지우고 for문을 빠져나옴
            if letters[j] == letters[j+1]:
                if 0 < j < len(letters)-2:
                    letters = letters[:j]+letters[j+2:]                    
                elif j == 0:
                    letters = letters[j+2:]
                else:
                    letters = letters[:j]
                break        
        # 중복이 발견되지 않았으면(for문 결과가 원본과 같으면) 중복이 모두 제거된 것
        if letters == original_letters:
            break
    return len(letters)
        

# Stack의 성질을 이용한 방법
def erase2(letters):
    # 중복을 제거한 문자열을 저장할 스택
    stack_result=[]
    # 원본 문자열을 저장할 스택
    stack=[]
    for letter in letters:
        stack.append(letter)
    
    # 문제에선 앞에서부터 중복을 체크하니 제일 앞의 원소를 pop
    
    while stack:
        if not stack_result:
            stack_result.append(stack.pop(0))

        # 원본문자열의 앞(pop0)과 중복을 제거한 문자열의 뒤(pop)를 비교
        stack_first = stack.pop(0)
        result_last = stack_result.pop()
        if stack_first == result_last:
            continue
        else:
            stack_result.append(result_last)
            stack_result.append(stack_first)
    
    return len(stack_result)

t = int(input())
for test in range(t):
    chars = input()
    print('#'+str(test+1), erase2(chars))