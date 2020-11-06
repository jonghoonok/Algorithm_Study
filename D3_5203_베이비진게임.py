import sys

sys.stdin = open("D3_5203_베이비진게임_input.txt", "r")


def babygin():
    player1 = [cards[0], cards[2]]
    player2 = [cards[1], cards[3]]
    # 플레이어 1이 카드 3장을 받는 시점부터 시작
    for i in range(4, 12):
        # 플레이어 1의 차례
        if i % 2 == 0:
            player1.append(cards[i])
            if check(player1):
                return 1
        # 플레이어 2의 차례
        else:
            player2.append(cards[i])
            if check(player2):
                return 2
    # 아무도 못 이겼다면 무승부
    return 0          


def check(arr):
    # 0부터 9까지의 수가 각각 몇 개나 들어있는지 저장
    check = [0]*10
    
    for num in arr:
        check[num] += 1

    # 연속하는 숫자의 갯수를 저장하는 변수
    cnt = 0
    for i in range(10):
        if check[i]:
            # 같은 숫자가 3개 이상이다: triple
            if check[i] > 2:
                return True
            cnt += 1
        else:
            cnt = 0
        # 연속하는 숫자가 3개 이상이다: run
        if cnt > 2:
            return True
    return False


t = int(input())
for test_case in range(t):
    cards = list(map(int, input().split()))
    print('#' + str(test_case + 1), babygin())