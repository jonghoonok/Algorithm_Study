lpv = []
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    lpv.append((L, P, V))

for i in range(len(lpv)):
    result = (lpv[i][2] // lpv[i][1]) * lpv[i][0]
    if lpv[i][2] % lpv[i][1] > lpv[i][0]:
        result += lpv[i][0]
    else:
        result += lpv[i][2] % lpv[i][1]

    print(f'Case {i+1}: {result}')