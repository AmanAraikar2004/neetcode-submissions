class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = [1] * n
        prefix = 1
        for i in range(n):
            temp[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            temp[i] *= suffix
            suffix *= nums[i]
        return temp