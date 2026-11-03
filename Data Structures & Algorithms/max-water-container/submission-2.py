class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        p1 = 0 
        p2 = len(heights) - 1
            
        max_area = 0 

        while p1 < p2: 
            area = min(heights[p1], heights[p2]) * (p2 - p1)

            if area > max_area: 
                max_area = area 
            
            if heights[p1] >= heights[p2]: 
                p2 -= 1 
            elif heights[p2] > heights[p1]: 
                p1 += 1 
            else: 
                break
        
        return max_area