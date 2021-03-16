n = int(input())
arr = [0]*(n+2)    # n = 1인 경우에 배열의 길이가 2기 되기 때문에 indexerror(arr[2])를 막기 위해 n+2로 선언
arr[1], arr[2] = 1, 2
for i in range(3, n+1):
    # 마지막에 10007로 나눈 나머지를 얻는거나 이거나 똑같음
    # 피보나치 1000을 하면 수가 너무 커지니 미리 나눠서 계산을 줄임
    arr[i] = (arr[i-1] + arr[i-2]) % 10007

print(arr[n])