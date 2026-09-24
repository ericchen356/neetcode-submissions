class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}

        for x in nums: 
            if x not in dict: 
                dict[x] = 1
            else: 
                return True
        
        return False
