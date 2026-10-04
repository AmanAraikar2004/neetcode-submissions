class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        n = prices[0]
        left, right = 0, 0
        for i in range(len(prices)):
            n = min(n, prices[i])
            m = max(m, prices[i] - n)
        return m