# 내 풀이: 케이스를 나눈 투 포인터인데 예외 발생하여 실패
def threeSum_1(nums):
        result = []
        nums.sort()

        # i, j, k는 음수1, 양수2 or 음수2, 양수1개의 조합 or 음수-0-양수 or 0-0-0으로 구성됨
        # 투 포인터를 이용하여 각각의 조합을 계산
        minus = []
        plus = []
        zero_cnt = 0
        for num in nums:
            if num < 0:
                minus.append(num)
            elif num > 0:
                plus.append(num)
            else:
                zero_cnt += 1
        
        # Case1: i가 음수고 j, k가 양수인 경우
        for i in range(len(minus)):
            # 중복제거: i가 같으면 j, k의 쌍도 다시 반복되기 때문에 skip
            if i > 0 and minus[i] == minus[i-1]:
                continue
            j, k = 0, len(plus)-1
            while j < k:
                if plus[j] + plus[k] < -minus[i]:
                    j += 1
                elif plus[j] + plus[k] > -minus[i]:
                    k -= 1
                else:
                    result.append([minus[i], plus[j], plus[k]])
                    j += 1
                    k -= 1
        # Case2: i, j가 음수고 k가 양수인 경우
        for k in range(len(plus)):
            if k > 0 and plus[k] == plus[k-1]:
                continue
            i, j = 0, len(minus)-1
            while i < j:
                if minus[i] + minus[j] < -plus[k]:
                    i += 1
                elif minus[i] + minus[j] > -plus[k]:
                    j -= 1
                else:
                    result.append([minus[i], minus[j], plus[k]])
                    i += 1
                    j -= 1
        
        # Case3: 0이 있는 경우
        if zero_cnt:
            if minus and plus:
                index = nums.index(0)
                left, right = index - 1, index + 1
                while left >= 0 and right < len(nums):
                    if -nums[left] > nums[right]:
                        right += 1
                    elif -nums[left] < nums[right]:
                        left -= 1
                    else:
                        result.append([nums[left], 0, nums[right]])
                        while left > 0 and nums[left] == nums[left-1]: left -= 1
                        while right < len(nums) - 1 and nums[right] == nums[right+1]: right += 1
                        left -= 1
                        right += 1

            # Case4: 0이 3개 이상 있는 경우
            if zero_cnt >= 3:
                result.append([0, 0, 0])
            

        return result


# 단순한 투 포인터
def threeSum_2(nums):
        result = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum < 0:
                    j += 1
                elif three_sum > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]: j += 1
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    j += 1
                    k -= 1
        return result

nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
print(threeSum_1(nums))