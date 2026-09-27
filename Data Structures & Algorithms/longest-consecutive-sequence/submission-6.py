class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        setRepresentation = set(nums)

        if len(nums) > 0: 
            current = 1 
            maxLength = 1

            for num in setRepresentation: 
                if num-1 not in setRepresentation: 
                    while (num + current) in setRepresentation: 
                        current += 1 
                        maxLength = max(maxLength, current)
                else: 
                    current = 1
    
        else: 
            return 0 

        return maxLength

            