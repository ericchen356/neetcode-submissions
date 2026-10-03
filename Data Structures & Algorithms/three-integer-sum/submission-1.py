class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        dict = {value : nums.count(value) for value in nums}

        p1, p2 = 0, 1 

        results = set()

        while p1 < len(nums) - 1: 
            while p2 < len(nums): 
                    
                twosum = nums[p1] + nums[p2] 
                complement = -twosum 
                triplet = [nums[p1], nums[p2], complement]
                
                valid = True 

                if complement in dict: 
                    for val in triplet: 
                        if triplet.count(val) > dict[val]:
                            valid = False

                    if valid == True: 
                        results.add(tuple(sorted(triplet)))
                    
                p2 += 1
                
            p1 += 1
            p2 = p1 + 1

        return [list(triplet) for triplet in results] 
            
