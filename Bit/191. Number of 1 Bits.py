# 1을 빼준 뒤 자기 자신과 AND연산 해주면 비트가 1개씩 빠짐
# 이유는 모르겠다..
def hammingWeight(self, n: int) -> int:
    result = 0
    while n:
        n &= n - 1
        result += 1
    return result