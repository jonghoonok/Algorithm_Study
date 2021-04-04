def trap_1(height) -> int:
    # 고인 물의 총량
    result = 0
    # 현재 보고 있는 고인 물: result에 더해줌
    water = 0

    # 왼쪽에서 오른쪽으로 이동하며 가장 높은 벽의 인덱스를 구함
    n = len(height)
    max_index = 0
    max_height = 0
    for i in range(n):
        # 벽의 높이가 갱신될 때마다 왼쪽으로 고여있는 물의 양을 결과에 더함
        if height[i] >= max_height:
            max_height = height[i]
            max_index = i
            if water:
                result += water
                water = 0
        # 현재 보고 있는 벽과 지금까지 본 벽 중에서 가장 높은 것의 차이만큼 물이 고임
        else:
            water += max_height - height[i]

    # 위의 과정을 마치면 가장 높은 벽 기준으로 왼쪽에 고인 물만 알 수 있음
    # 오른쪽 끝에서 가장 높은 벽으로 이동하며 동일한 방식으로 물이 고인 양을 구함
    water = 0
    max_height = 0
    for i in range(n-1, max_index-1, -1):
        if height[i] >= max_height:
            max_height = height[i]
            if water:
                result += water
                water = 0
        else:
            water += max_height - height[i]
    
    return result


# 내 풀이랑 논리는 동일한데 조금 더 간결함
def trap_1(height) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume


# 스택을 이용한 풀이
def trap_2(height):
    stack = []
    volume = 0

    for i in range(len(height)):
        # 낮아지다가 높아지는 지점을 만나면 높이차만큼 물을 채운다
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            # pop하자마자 스택이 비면 stop: 올라가는 구간에서는 마지막으로 제일 높은 벽만 남기게 됨
            if not stack:
                break

            distance = i - stack[-1] -1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)
    
    return volume

height = [4,2,0,3,2,5]
print(trap(height))