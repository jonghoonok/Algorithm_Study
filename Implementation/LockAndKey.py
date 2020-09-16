def rotate_by_90_degree(matrix):
    n = len(matrix)         # 행 길이
    m = len(matrix[0])      # 열 길이
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            # 시계 방향으로 90도 회전시킨 결과를 저장
            result[j][n-i-1] = matrix[i][j]
    return result


def check(new_lock):
    lock_length = len(new_lock)//3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for rotation in range(4):
        key = rotate_by_90_degree(key)
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 열쇠 끼우기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock):
                    return True
                # 열쇠를 빼고 원상복구
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]               
    
    return False
