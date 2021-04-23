def maxProfit(prices) -> int:
    # 하락이 시작되면 전고점에서 팔고 상승이 시작되면 저점에서 삼
    down = up = False

    low_price = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            up = True
            # 하락장에서 상승이 시작됐으면 바로 삼
            if down:
                low_price = prices[i-1]
            down = False
        else:
            down = True
            # 상승장에서 하락이 시작됐으면 판다
            if up:
                profit += prices[i-1] - low_price
            up = False
    
    if up:
            profit += prices[i-1] - low_price
    
    return profit

# 더 간결한 코드
def maxProfit(prices) -> int:
    result = 0
    for i in range(len(prices) - 1):
        if prices[i+1] > prices[i]:
            result += prices[i+1] - prices[i]
    return result