class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s) 
        result = 0 

        for char in chars: 
            l = 0
            count = 0 

            # increase window size 
            for r in range(len(s)): 
                if s[r] == char: 
                    count += 1 

                # while window invalid 
                while (r-l+1 - count) > k: 
                    if s[l] == char: 
                        count -= 1
                    l += 1

                # update max 
                result = max(r-l+1, result)

        return result 