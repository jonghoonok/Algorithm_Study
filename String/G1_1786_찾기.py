import sys

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

n = len(T)
m = len(P)

# P의 각 위치마다 실패함수의 값 저장
# 실패함수: 해당 인덱스까지의 문자열에서 접두사와 접미사가 일치하는 최대 길이(lps)
fail = [0]*(m)
j = 0
# i = 0일 때는 실패함수가 0임이 자명하므로 pass
for i in range(1, m):
    while j > 0 and P[i] != P[j]:
        j = fail[j-1]
    # i번째 인덱스까지의 문자열에서 현재 j가 위치한 자리의 길이(j+1)가 실패함수의 값이 됨    
    if P[i] == P[j]:
        # j를 오른쪽으로 한 칸 이동
        j += 1
        fail[i] = j
    i += 1

# T와 P를 비교
j = 0
# T와 P가 일치하는 지점의 인덱스를 저장
result = []
for i in range(n):
    # 불일치가 발생하면 fail값을 "따라감"
    while j > 0 and T[i] != P[j]:
        j = fail[j-1]
    if T[i] == P[j]:
        # 문자열 매칭 성공
        if j == m-1:
            result.append(i-m+2)
            # 계속 탐색: fail값을 따라감
            j = fail[j]
        else:
            j += 1

print(len(result))
print(' '.join(map(str, result)))