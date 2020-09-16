def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        temp = len(s)
        
        j = 0
        cnt = 0
        while j+i*2 <= len(s) :            
            if s[j:j+i] == s[j+i:j+i*2]:
                cnt += 1
            else:
                if cnt:
                    temp -= i*cnt - 1                                 
                    cnt = 0
            j += i
        if cnt:
            temp -= i*cnt - 1                                 
            
        if temp < answer:
            answer = temp
    return answer

for _ in range(5):
    words = input()
    print(solution(words))

# aabbaccc
# ababcdcdababcdcd
# abcabcdede
# abcabcabcabcdededededede
# xababcdcdababcdcd