n = int(input())
m = int(input())
s = input()

ans = 0     # P_N이 몇 개나 포함되어 있는지 나타내는 변수
cnt = 0     # O의 갯수를 카운트하여 N이 될 때마다 ans += 1
idx = 1     # 슬라이딩 윈도우의 가운데 인덱스

while idx < m-1:
    if s[idx-1:idx+2] == "IOI":
        cnt += 1
        if cnt == n:
            cnt -= 1
            ans += 1
        idx += 1          # 두 칸씩 이동해야 함
    else:
        cnt = 0
    idx += 1              # IOI가 아닌 경우 한 칸만 이동

print(ans)