def common_square(square1, square2):
    x1, y1, p1, q1 = square1[0], square1[1], square1[2], square1[3]
    x2, y2, p2, q2 = square2[0], square2[1], square2[2], square2[3]
    
    # 안 겹치는 경우
    # 1번 직사각형의 왼쪽, 위, 오른쪽, 아래에 있는 경우
    if (p2 < x1) or (p2 == x1 and (q2 < y1 or q1 < y2) ) or (q1 < y2) or (q1 == y2 and (p2 < x1 or p1 < x2) ) or (p1 < x2) or (p1 == x2 and (q2 < y1 or q1 < y2) ) or (q2 < y1) or (q2 == y1 and (p2 < x1 or p1 < x2)):
        return 'd'
    # 선분으로 겹치는 경우
    # 1번 사각형의 왼쪽, 위, 오른쪽, 아래
    elif (x1 == p2 and y1 < q2 and y2 < q1) or (q1 == y2 and x1 < p2 and x2 < p1) or (p1 == x2 and y1 < q2 and y2 < q1) or (y1 == q2 and x1 < p2 and x2 < p1):
        return 'b'  
    # 점으로 겹치는 경우
    # 1번 사각형의 왼쪽 위, 오른쪽 위, 오른쪽 아래, 왼쪽 아래
    elif (x1 == p2 and q1 == y2) or (p1 == x2 and q1 == y2) or (p1 == x2 and y1 == q2) or (x1 == p2 and y1 == q2):
        return 'c'
    # 직사각형으로 겹치는 경우
    else:
        return 'a'


squares = [list(map(int, input().split())) for _ in range(4)]
for i in range(4):
    print(common_square(squares[i][:4], squares[i][4:]))