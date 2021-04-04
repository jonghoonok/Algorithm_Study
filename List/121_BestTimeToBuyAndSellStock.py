def maxProfit_1(prices) -> int:
        low = prices[0]
        high = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            # 고점이 갱신될 때마다 얻을 수 있는 수익을 저장
            if prices[i] > high:
                high = prices[i]
                profit = max(profit, high - low)
            
            # 저점이 갱신되면 고점을 초기화하여 새로운 저점 이후에 얻을 수 있는 수익을 저장할 수 있도록 함
            elif prices[i] < low:
                low = prices[i]
                high = prices[i]

        return profit


# 책의 풀이: 모든 가격에 대해 갱신함 - 내 풀이보다 살짝 느림
def maxProfit_2(prices) -> int:
        profit = 0
        min_price = 10000

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        
        return profit

prices = [7,6,4,3,1]
print(maxProfit(prices))