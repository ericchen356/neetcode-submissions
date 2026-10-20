class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = {}

        # create freq map of needed chars 
        for char in t: 
            need[char] = need.get(char, 0) + 1 
        
        required = len(need) # num of required chars 
        window = {} 
        formed = 0 # num of chars that the window has enough of

        best_len = float("inf")
        best_start = 0 
        left = 0 

        for right in range(len(s)): 
            # grow window until valid and update window map 
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]: 
                formed += 1 
            
            # shrink window until invalid again 
            while formed == required:
                # update best length and best start
                if right - left + 1 < best_len:
                    best_len = right - left + 1 
                    best_start = left 
                
                # remove from window 
                left_char = s[left]
                window[left_char] -= 1 

                if left_char in need and window[left_char] < need[left_char]: 
                    formed -= 1 

                left += 1 
        
        if best_len == float("inf"): 
            return ""
        
        return s[best_start : best_start + best_len]
