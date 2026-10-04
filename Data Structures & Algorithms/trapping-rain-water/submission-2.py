class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        running_max = 0
        for i in range(len(height)):
            running_max = max(running_max, height[i])
            left_max.append(running_max)
        running_max = 0
        right_max = []
        for i in range(len(height) - 1, -1, -1):
            running_max = max(running_max, height[i])
            right_max.append(running_max)
        right_max.reverse()
        water_above_i = 0
        for i in range(len(height)):
            temp = min(left_max[i], right_max[i]) - height[i]
            if temp >= 0:
                water_above_i += temp
        return water_above_i