import sys

sys.stdin = open("D3_4047_input.txt", "r")


def card_count():
    cnt = [[0]*13 for _ in range(4)]
    
    i = 0  
    while i < len(cards):        
        if cards[i] == 'S':
            if cnt[0][int(cards[i+1:i+3])-1]:
                print("ERROR")
                return
            else:
                cnt[0][int(cards[i+1:i+3])-1] += 1
        elif cards[i] == 'D':
            if cnt[1][int(cards[i+1:i+3])-1]:
                print("ERROR")
                return
            else:
                cnt[1][int(cards[i+1:i+3])-1] += 1
        elif cards[i] == 'H':
            if cnt[2][int(cards[i+1:i+3])-1]:
                print("ERROR")
                return
            else:
                cnt[2][int(cards[i+1:i+3])-1] += 1
        else:            
            if cnt[3][int(cards[i+1:i+3])-1]:
                print("ERROR")
                return
            else:
                cnt[3][int(cards[i+1:i+3])-1] += 1
        i += 3
    
    for i in range(4):
        temp = 0
        for j in range(13):
            if cnt[i][j]:
                temp += 1
        print(13-temp, end=" ")
    print()

# 딕셔너리를 이용하여 더 간결한 구현이 가능
def card_count2():
    card_dic = {
        'S': [],
        'D': [],
        'H': [],
        'C': [],
        }
    
    i = 0
    while i < len(cards):        
        if int(cards[i+1:i+3]) not in card_dic[cards[i]]:
            card_dic[cards[i]].append(int(cards[i+1:i+3]))
        else:
            print('ERROR')
            return
        i += 3
    
    for key in card_dic.keys():
        print(13 - len(card_dic[key]), end=" ")
    print()
    

T = int(input())
for test_case in range(T):
    cards = input()
    print('#' + str(test_case + 1), end=" ")
    card_count2()
