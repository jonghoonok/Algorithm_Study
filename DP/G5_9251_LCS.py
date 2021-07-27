string1 = input()
string2 = input()

n = len(string1)
m = len(string2)

string1 = ' '+string1
string2 = ' '+string2

LCS = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if string2[j] == string1[i]:
            LCS[i][j] = LCS[i-1][j-1]+1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[-1][-1])