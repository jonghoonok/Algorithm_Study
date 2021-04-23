def fib(self, n: int) -> int:
    if not n:
        return 0

    dp = [0]*(n+1)
    dp[0], dp[1] = 0, 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]


def fib(self, n: int) -> int:
    if n <= 1:
        return n
    if dp[n]:
        return dp[n]
    dp[n] = self.fib(n-1) + self.fib(n-2)
    return dp[n]