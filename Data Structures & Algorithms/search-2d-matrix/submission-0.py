class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            left = 0
            right = len(i) - 1
            mid = (left + right) // 2
            while left <= right:
                if i[mid] == target:
                    return True
                if i[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                mid = (left + right) // 2
        return False