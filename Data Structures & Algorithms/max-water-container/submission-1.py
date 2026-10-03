class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        k = 0
        while left < right:
            m = (right - left) * min(heights[left], heights[right])
            k = max(k, m)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return k