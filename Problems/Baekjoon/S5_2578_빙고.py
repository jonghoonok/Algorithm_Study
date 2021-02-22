def bingo():
    cnt = 0         # 현재 부르고 있는 번호가 몇 번째인지

    while(cnt < 25):
        target = mc_numbers[cnt // 5][cnt % 5]
        update(target)    # 사회자가 부른 번호를 철수의 테이블에서 찾아 0으로 만들어 줌
        if(cnt > 10):   # 최소 숫자를 12개 불러야 빙고 3개가 나오기 때문에 cnt 11일때부터 검사
            if num_of_bingo() >= 3:
                return cnt+1
        cnt += 1    

def update(num):
    for i in range(5):
        for j in range(5):
            if my_numbers[i][j] == num:
                my_numbers[i][j] = 0
                return


# 현재 테이블에 빙고가 몇 개인지 검사하는 함수
def num_of_bingo():
    row = 0
    column = 0
    diagonal = 0

    for i in range(5):
        if not (my_numbers[i][0] or my_numbers[i][1] or my_numbers[i][2] or my_numbers[i][3] or my_numbers[i][4]):
            row += 1
    for j in range(5):
        if not (my_numbers[0][j] or my_numbers[1][j] or my_numbers[2][j] or my_numbers[3][j] or my_numbers[4][j]):
            column += 1
    if not (my_numbers[0][0] or my_numbers[1][1] or my_numbers[2][2] or my_numbers[3][3] or my_numbers[4][4]):
        diagonal += 1
    if not (my_numbers[0][4] or my_numbers[1][3] or my_numbers[2][2] or my_numbers[3][1] or my_numbers[4][0]):
        diagonal += 1

    return row + column + diagonal


my_numbers = [list(map(int, input().split())) for _ in range(5)]
mc_numbers = [list(map(int, input().split())) for _ in range(5)]
print(bingo())