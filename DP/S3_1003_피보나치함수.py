t = int(input())
for _ in range(t):
    n = int(input())
    # fibo(index)가 호출되는 횟수를 담은 배열
    cnts = [0]*(n+2)    # n = 0인 경우에 배열의 길이가 1이 되기 때문에 항상 2 이상을 보장하기 위해 n+2로 선언
    cnts[n] = 1
    for i in range(n, 1, -1):
        cnts[i-1] += cnts[i]
        cnts[i-2] += cnts[i]
    print(cnts[0], cnts[1])