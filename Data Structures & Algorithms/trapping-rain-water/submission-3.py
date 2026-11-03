class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: 
            return 0
        
        l = 0 
        r = len(height) - 1
        res = 0 
        rightMax = height[-1]
        leftMax = height[0]

        while l < r: 

            if leftMax < rightMax: 
                res += leftMax - height[l]
                l += 1 
                leftMax = max(leftMax, height[l])
            else: 
                res += rightMax - height[r]
                r -= 1 
                rightMax = max(rightMax, height[r])

        return res 

