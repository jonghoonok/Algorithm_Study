# 기본 풀이
def numJewelsInStones_1(self, jewels: str, stones: str) -> int:
    freqs = {}

    for char in stones:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1
    
    result = 0
    for char in jewels:
        if char in freqs:
            result += freqs[char]

    return result


# defaultdict를 이용
def numJewelsInStones_2(self, jewels: str, stones: str) -> int:
    freqs = collections.defaultdict(int)
    cnt = 0

    for char in stones:
        freqs[char] += 1

    for char in jewels:
        cnt += freqs[char]

    return cnt


# Counter를 이용 
def numJewelsInStones_3(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        cnt = 0

        for char in jewels:
            cnt += freqs[char]

        return cnt


# Pythonic
def numJewelsInStones_3(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)