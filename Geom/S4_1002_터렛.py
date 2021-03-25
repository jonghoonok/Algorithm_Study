t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and x2 == y2:
        # 무한대인 경우: 동일한 원
        if r1 == r2:
            print(-1)
        # 못 만나는 경우: 동심원
        else:
            print(0)
    else:
        dist = (x1 - x2)**2 + (y1 - y2)**2
        rad_square = (r1 + r2)**2
        # 한 점에서만 만나는 경우: 외접
        if dist == rad_square:
            print(1)
        else:
            # 못 만나는 경우
            if dist > rad_square:
                print(0)
            else:
                # 한 점에서만 만나는 경우: 내접
                if dist == (r1-r2)**2:
                    # 이 좌표가 지도 상에 존재할 수 있는지 체크
                    if r1 > r2:
                        # r1이 더 크면 x2, y2방향으로 r1만큼 움직인 지점이 내접점
                        x3 = x1 + (x2 - x1)*abs(r1 / (x2 - x1))
                        y3 = y1 + (y2 - y1)*abs(r1 / (y2 - y1))
                        if -10000 <= x3 <= 10000 and -10000 <= y3 <= 10000:
                            print(1)
                        else:
                            print(0)
                    else:
                        # r2가 더 크면 x1, y1방향으로 r2만큼 움직인 지점이 내접점
                        x3 = x2 + (x1 - x2)*abs(r2 / (x2 - x1))
                        y3 = y2 + (y1 - y2)*abs(r2 / (y2 - y1))
                        if -10000 <= x3 <= 10000 and -10000 <= y3 <= 10000:
                            print(1)
                        else:
                            print(0)
                # 한 원이 다른 원을 포함하는 경우
                elif dist < (r1-r2)**2:
                    print(0)
                # 두 점에서 만나는 경우
                else:
                    # 이 좌표가 지도 상에 존재할 수 있는지 체크
                    # x1, y1이 x2, y2를 향하는 단위벡터를 각각 왼쪽, 오른쪽으로 30도씩 돌리고
                    # r1의 길이만큼 곱해준 후 x1, y1을 더해주면 두 점의 좌표가 나옴
                    # 이렇게까지 해야될까?

                    # 벡터의 회전
                    # x' = cos_theta * x - sin_theta * y
                    # y' = sin_theta * x + cos_theta * y
                    x3 = x1 + r1 * 
                    # print(2)