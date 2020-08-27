import sys

sys.stdin = open("D4_1218_input.txt", "r")


def parenthesis_test(words):
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    for element in words:
        if element == '(':
            list1.append(element)
        elif element == '[':
            list2.append(element)
        elif element == '{':
            list3.append(element)
        elif element == '<':
            list4.append(element)
        elif element == ')':
            if list1:
                list1.pop()
            else:
                return 0
        elif element == ']':
            if list2:
                list2.pop()
            else:
                return 0
        elif element == '}':
            if list3:
                list3.pop()
            else:
                return 0
        elif element == '>':
            if list4:
                list4.pop()
            else:
                return 0
    if list1 or list2 or list3 or list4:
        return 0
    else:
        return 1


for test_case in range(10):
    n = int(input())
    parenthesis_list = input()
    print('#'+str(test_case+1), parenthesis_test(parenthesis_list))
    