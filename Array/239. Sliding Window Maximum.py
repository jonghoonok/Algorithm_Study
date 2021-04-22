import collections

def maxSlidingWindow(nums, k: int):
        window = collections.deque(nums[:k])
        result = []
        max_value = float('-inf')
        
        for i in range(k-1, len(nums)):
            window.append(nums[i])

            if max_value == float('-inf'):
                max_value = max(window)
            elif nums[i] > max_value:
                max_value = nums[i]

            result.append(max_value)

            if max_value == window.popleft():
                max_value = float('-inf')

        return result

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))