import collections

# Pythonic: 아주 치사한 방법이 아닐까...
def topKFrequent_1(nums, k):
    freqs = collections.Counter(nums)
    return [num[0] for num in freqs.most_common(k)]



# defaultdict와 우선순위 큐를 이용
def topKFrequent_2(nums, k):
    freqs = collections.defaultdict(int)
    freqs_q = []
    for num in nums:
        if num not in freqs:
            freqs[num] = 1
        else:
            freqs[num] += 1
    
    for key, value in freqs.items():
        heapq.heappush(freqs_q, (-value, key))

    result = []
    for _ in range(k):
        result.append(heapq.heappop(freqs_q)[1])
    
    return result

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent_2(nums, k))