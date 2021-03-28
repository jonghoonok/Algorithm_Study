import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    # 전화번호부
    book = []
    flag = True
    for i in range(n):
        tel_num = sys.stdin.readline().rstrip()
        book.append(tel_num)
    
    book.sort()
    print(book)
    for i in range(n-1):
        # 문자열은 정렬하면 수 크기의 오름차순이 아니라 사전순으로 정렬됨
        # '123'다음에는 '124'가 아니라 '1234'가 옴
        # 따라서 붙어있는 두 번호만 비교하면 OK
        if book[i] == book[i+1][:len(book[i])]:
            flag = False
            break

    if flag:
        print('YES')
    else:
        print('NO')