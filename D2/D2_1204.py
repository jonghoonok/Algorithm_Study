t = int(input())

for i in range(t):
    n = input()
    score_list = list(map(int, input().split()))
    score_list2 = [0 for _ in range(101)]
    for j in range(1000):
        score_list2[score_list[j]] += 1
    max_score = 0
    temp = 0
    for k in range(101):        
        if score_list2[100-k] > temp:
            max_score = 100-k
            temp = score_list2[100-k]
    print('#'+n, max_score)