class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2
            hours = sum((p + mid - 1) // mid for p in piles)

            if hours <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
