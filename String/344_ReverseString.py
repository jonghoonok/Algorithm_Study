# Two Pointer
def reverseString_1(self, s: List[str]) -> None:
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Pythonic1
def reverseString_2(self, s: List[str]) -> None:
    s.reverse()


# Pythonic2
def reverseString_3(self, s: List[str]) -> None:
    # Space restrictions O(1): s[:] is needed
    s[:] = s[::-1]