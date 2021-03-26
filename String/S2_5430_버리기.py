import sys

t = int(input())
for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(',')

    # 현재 배열이 뒤집혔는지 나타내는 변수
    # R이 나올때마다 뒤집으면 오래걸리므로 마지막에 한 번만 뒤집음
    flag = 0
    # 앞에서 빼는 숫자와 뒤에서 빼는 숫자의 갯수
    num = [0, 0]
    for char in p:
        if char == 'R':
            flag = 1 - flag
        else:
            # 뒤집힌 상태라면 뒤에서 뺄 수를 하나 추가
            if flag:
                num[1] += 1
            # 뒤집힌 상태가 아니라면 앞에서 뺄 수를 하나 추가
            else:
                num[0] += 1
    
    if num[0]+num[1] > n:
        print("error")
    else:
        arr = arr[num[0]:n-num[1]]
        if flag and arr:
            arr.reverse()
        print("["+','.join(arr)+"]")