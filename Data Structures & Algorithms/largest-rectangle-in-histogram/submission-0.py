class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0
        for i in range(len(heights)):
            while stack and heights[i] < stack[-1][1]:
                temp = stack.pop()
                height = temp[1]
                right = i
                if not stack:
                    left = -1
                else:
                    left = stack[-1][0]
                width = right - left - 1
                area = height * width
                best = max(best, area)
            stack.append((i, heights[i]))

        while stack:
                temp = stack.pop()
                height = temp[1]
                right = len(heights)
                if not stack:
                    left = -1
                else:
                    left = stack[-1][0]
                width = right - left - 1
                area = height * width
                best = max(best, area)
        
        return best
