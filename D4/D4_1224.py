import sys
sys.stdin = open("D4_1224_input.txt", "r")


def make_forth(code):
    stack = []
    result = []
    for element in code:
        if element not in operator and element not in parenthesis:
            result.append(element)
        else:
            if element == ')':
                while True:
                    pop = stack.pop()
                    if pop == '(':
                        break
                    result.append(pop)
            else:
                if element in ['+', '-']:
                    while stack[-1] != '(':
                        result.append(stack.pop())
                    stack.append(element)
                elif element in ['*', '/']:
                    while stack[-1] not in ['(', '+', '-']:
                        result.append(stack.pop())
                    stack.append(element)
                else:
                    stack.append(element)
    return result


def forth(numbers):    
    stack = []    
    for i in range(len(numbers)): 
        if numbers[i] not in operator:
            stack.append(int(numbers[i]))
        else:
            num1, num2 = stack.pop(), stack.pop()            
            if numbers[i] == '+':
                stack.append(num2+num1)
            elif numbers[i] == '-':
                stack.append(num2-num1)
            elif numbers[i] == '*':
                stack.append(num2*num1)
            else:
                stack.append(num2//num1)
        if i == len(numbers) - 1:
            return stack.pop()


operator = ['+', '-', '*', '/']
parenthesis = ['(', ')']
for test in range(10):
    n = int(input())
    code = list(input())    
    forth_code = make_forth(code)
    print('#'+str(test+1), forth(forth_code))