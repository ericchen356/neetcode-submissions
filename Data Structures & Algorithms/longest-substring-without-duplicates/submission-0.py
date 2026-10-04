class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        maximum = 0

        while r < len(s): 
            while s[r] in s[l:r]: 
                l += 1
            
            maximum = max(r-l+1, maximum)

            r += 1
        
        return maximum 