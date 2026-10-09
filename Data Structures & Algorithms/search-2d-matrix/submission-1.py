class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid_row = (top + bottom) // 2
            if matrix[mid_row][-1] < target:
                top = mid_row + 1
            elif matrix[mid_row][0] > target:
                bottom = mid_row - 1
            else:
                break
        
        mid_row = (top + bottom) // 2

        left = 0
        right = len(matrix[mid_row]) - 1
        mid = (left + right) // 2

        while left <= right:
            if matrix[mid_row][mid] == target:
                return True
            if matrix[mid_row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            mid = (left + right) // 2
        
        return False