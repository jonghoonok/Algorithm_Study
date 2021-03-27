str1 = input()
str2 = input()
n = len(str1)
m = len(str2)

str1 = ' '+str1
str2 = ' '+str2
# 행은 str1, 열은 str2
LCS = [['']*(m+1) for _ in range(n+1)]

# DP
for i in range(1, n+1):
    for j in range(1, m+1):
        if str1[i] == str2[j]:
            LCS[i][j] = LCS[i-1][j-1]+str1[i]
        else:
            if len(LCS[i-1][j]) >= len(LCS[i][j-1]):
                LCS[i][j] = LCS[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]

print(len(LCS[n][m]))
print(LCS[n][m])