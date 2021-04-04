# 책의 풀이: 왼쪽의 곱셈 결과와 오른쪽의 곱셈 결과를 곱한다
# append가 시간을 많이 차지할 것이라 생각했는데 별 차이가 안 남
def productExceptSelf(nums):
        n = len(nums)
        result = [0]*n
        p = 1
        # 왼쪽 곱셈: i보다 왼쪽에 있는 모든 수를 곱한 값 p를 저장
        for i in range(n):
            result[i] = p
            p *= nums[i]
        p = 1
        # 오른쪽 곱셈: i보다 왼쪽에 있는 모든 수를 곱한 값에 오른쪽의 모든 수를 곱한 값 p를 곱해서 저장
        for i in range(n-1, -1, -1):
            result[i] *= p
            p *= nums[i]
        return result

nums = [1,2,3,4]
print(productExceptSelf(nums))