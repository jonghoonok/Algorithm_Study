def Z(n, r, c, cur):
    if n == 0:
        return cur

    # (r,c)가 몇 사분면에 위치하는지 판단
    if r < 2**(n-1):
        # 왼쪽 위
        if c < 2**(n-1):
            return Z(n-1, r, c, cur)
        # 오른쪽 위
        else:
            return Z(n-1, r, c - 2**(n-1), cur + 2**(2*n-2))
    else:
        # 왼쪽 아래
        if c < 2**(n-1):
            return Z(n-1, r - 2**(n-1), c, cur + 2*2**(2*n-2))
        # 오른쪽 아래
        else:
            return Z(n-1, r - 2**(n-1), c - 2**(n-1), cur + 3*2**(2*n-2))


n, r, c = map(int, input().split())
print(Z(n, r, c, 0))