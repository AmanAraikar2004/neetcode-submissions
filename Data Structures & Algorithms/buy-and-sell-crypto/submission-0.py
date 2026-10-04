class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                m = max(m, prices[j] - prices[i])
        return m