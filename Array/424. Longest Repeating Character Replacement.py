def characterReplacement(self, s: str, k: int) -> int:
    l = r = 0
    cnt = collections.Counter()

    # r포인터를 하나씩 이동시키며 윈도우를 늘려 나감
    for r in range(1, len(s)+1):
        cnt[s[r-1]] += 1
        max_char = cnt.most_common(1)[0][1]

        # r과 l의 간격을 최대한 길게 유지하다가 바꿔야 하는 문자 수가 k를 넘으면 l 포인터를 이동시킴
        if r - l - max_char > k:
            cnt[s[l]] -= 1
            l += 1
    return r - l