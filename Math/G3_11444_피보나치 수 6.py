#                n
#       | 1   1 |    | F(n+1)  F(n)  |
# A^n = |       |  = |               |
#       | 1   0 |    |  F(n)  F(n-1) |
def pow(n):
    if n == 0 or n == 1:
        return A

    ret = pow(n//2)
    ret = multiply(ret, ret)
    if n % 2 == 1:
        ret = multiply(ret, A)
    
    return ret


def multiply(mat1, mat2):
    result = [[0, 0], [0, 0]]

    result[0][0] = (mat1[0][0]*mat2[0][0] + mat1[0][1]*mat2[1][0]) % MOD
    result[0][1] = (mat1[0][0]*mat2[0][1] + mat1[0][1]*mat2[1][1]) % MOD
    result[1][0] = (mat1[1][0]*mat2[0][0] + mat1[1][1]*mat2[1][0]) % MOD
    result[1][1] = (mat1[1][0]*mat2[0][1] + mat1[1][1]*mat2[1][1]) % MOD

    return result


MOD = 1000000007
A = [[1, 1], [1, 0]]
n = int(input())
print(pow(n)[0][1])