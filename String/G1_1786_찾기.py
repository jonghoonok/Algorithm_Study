T = input()
P = input()

# P의 각 위치마다 실패함수의 값 저장
# 접두사와 접미사가 일치하는 최대 길이 구하기
fail = [0]*(len(P))
j = 0
i = 1
while i < len(P):
    while j > 0 and P[i] != P[j]:
        j = fail[j-1]
    if P[i] == P[j]:
        j += 1
        fail[i] = j
    i += 1

# T와 P를 비교
i = 0
while i < len(T):
    flag = True
    for j in range(len(P)):
        if T[j] != P[j]:
            # 불일치가 발생하면 skip
            i += j - fail[j] + 1
            flag = False
            break
    # P의 모든 원소에 대해 불일치가 발생하지 않았으면 현재 인덱스 i가 정답
    if flag:
        print(i)
        break