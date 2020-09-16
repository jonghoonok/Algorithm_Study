def max_card():
    min_max = 10000
    for i in range(M):
        if card_list[0][i] < min_max:
            min_max = card_list[0][i]
            
    for i in range(N):        
        temp = 10000
        for j in range(M):
            if card_list[j][i] < temp:
                temp = card_list[j][i]
            if temp < min_max:
                break
        if temp > min_max:
            min_max = temp
    return min_max
            


N, M = map(int, input().split())
card_list = [list(map(int, input().split())) for _ in range(N)]
print(max_card())