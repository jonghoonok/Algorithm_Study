n = int(input())
stair = [0]*n
# 한 계단 을 연속해서 0번, 1번 밟은 경우 각각에 대해 해당 계단의 최대 점수를 저장 
# 한 계단씩 연속해서 2번 밟으면 3개의 연속한 계단을 밟는 것이 되므로 안 됨
score = [[0]*2 for _ in range(n)]
for i in range(n):
    stair[i] = int(input())

# 첫 번째 계단은 한 칸만 올라갈 수 있음
score[0][1] = stair[0]
if n > 1:
    score[1][0] = stair[1]
    score[1][1] = score[0][1] + stair[1]    # 1번 계단을 밟고 그 다음 2번 계단을 밟음

for i in range(2, n):
    # 2칸 올라오는 경우
    score[i][0] = max(score[i-2]) + stair[i]    
    # 1칸 올라오는 경우
    score[i][1] = score[i-1][0] + stair[i]  

print(max(score[n-1]))