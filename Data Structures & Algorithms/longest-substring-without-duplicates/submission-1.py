class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set() 
        l = 0 
        maximum = 0 

        for r in range(len(s)): 

            # if window invalid
            while s[r] in chars:
                # move left edge 
                chars.remove(s[l])
                l += 1   

            # increase window size
            chars.add(s[r])
            maximum = max(maximum, r-l+1)
        
        return maximum 