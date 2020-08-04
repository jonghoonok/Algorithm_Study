import sys

sys.stdin = open("D2_4834_input.txt", "r")

def cards(num, words):
    # 카드 번호를 리스트로 만들고 각각의 카드 갯수를 체크리스트에 기입
    card_list = [int(words[i]) for i in range(num)]
    check_list = [0] * 10
    for j in range(num):
        check_list[card_list[j]] += 1
    
    # 가장 갯수가 많은 카드의 번호를 card, 그 장수를 num에 저장
    card = 0
    num = 0
    for k in range(10):
        if num <= check_list[k]:
            card = k
            num = check_list[k]
    return card , num

t = int(input())

for test_case in range(t):
    n = int(input())
    a = input()
    num1, num2 = cards(n, a)
    print('#'+str(test_case+1), num1, num2)