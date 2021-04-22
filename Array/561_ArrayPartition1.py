# 내 풀이: 일종의 동적계획법(상위 57%)
def arrayPairSum_1(nums) -> int:
    result = 0
    nums.sort()
    for i in range(len(nums)):
        # 2개의 원소가 있으면 무조건 1번째, 4개면 1, 3번째 이런식으로 선택하는 것이 최대
        # 따라서 2n개의 원소가 있으면 인덱스가 짝수인 수의 합을 구하면 된다
        if i % 2 == 0:
            result += nums[i]
    return result


# 내 풀이2: 슬라이싱만 했을 뿐인데 상위 3.01%
def arrayPairSum_2(nums) -> int:
    nums.sort()
    return sum(nums[::2])


# 2랑 거의 동일한데 어째선지 살짝 느림
def arrayPairSum_3(nums) -> int:
    return sum(sorted(nums)[::2])


nums = [1,4,3,2]
print(arrayPairSum_2(nums))