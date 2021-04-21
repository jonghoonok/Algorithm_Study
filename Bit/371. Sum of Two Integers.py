def getSum(self, a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    a_bin = bin(a & MASK)[2:].zfill(32)
    b_bin = bin(b & MASK)[2:].zfill(32)
    result = []

    carry = 0
    for i in range(32):
        A = int(a_bin[31-i])
        B = int(b_bin[31-i])

        Q1 = A & B
        Q2 = A ^ B
        Q3 = Q2 & carry
        sum = carry ^ Q2
        carry = Q1 | Q3

        result.append(str(sum))
    if carry:
        result.append('1')

    ans = int(''.join(result[::-1]), 2) & MASK
    # 음수 처리: 왜 이렇게 하는지는 파이썬 알고리즘 인터뷰의 544페이지 참고
    if ans > 0x7FFFFFFF:
        ans = ~(ans ^ MASK)

    return ans

# 좀 더 간단한 풀이 
def getSum(self, a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    while b != 0:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

    if a > 0x7FFFFFFF:
        a = ~(a ^ MASK)
    return a