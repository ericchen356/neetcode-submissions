class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0 
        bottom = len(matrix) - 1

        while top <= bottom: 
            mid = (top + bottom) // 2

            if matrix[mid][0] > target: 
                bottom = mid - 1
            elif matrix[mid][-1] < target: 
                top = mid + 1 
            else: 
                break
        else: 
            return False
        
        row = mid 

        l, r = 0, len(matrix[row]) - 1 

        while l <= r: 
            m = (l+r) // 2
            if target < matrix[row][m]: 
                r = m - 1
            elif target > matrix[row][m]: 
                l = m + 1 
            else: 
                return True
        
        return False 


            