def hammingDistance(self, x: int, y: int) -> int:
    result = 0
    temp = x ^ y
    while temp:
        if temp % 2:
            result += 1
        temp = temp >> 1
    return result

# bin을 활용    
def hammingDistance(self, x: int, y: int) -> int:
    return bin(x ^ y).count('1')