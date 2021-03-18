string1 = input()
string2 = input()

n = len(string1)
m = len(string2)

string1 = ' '+string1
string2 = ' '+string2

LCS = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if string2[j] == string1[i]:
            LCS[i][j] = LCS[i-1][j-1]+1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[-1][-1])