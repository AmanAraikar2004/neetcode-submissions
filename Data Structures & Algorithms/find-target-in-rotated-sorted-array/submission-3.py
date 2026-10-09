class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Q1: is the LEFT half sorted?
            if nums[left] <= nums[mid]:
                # Q2: is target inside the left half's bounds?
                if nums[left] <= target < nums[mid]:      # blank 1, blank 2
                    right = mid - 1              # blank 3
                else:
                    left = mid + 1               # blank 4
            else:
                # right half is sorted
                if nums[mid] < target <= nums[right]:      # blank 5, blank 6
                    left = mid + 1               # blank 7
                else:
                    right = mid - 1             # blank 8

        return -1