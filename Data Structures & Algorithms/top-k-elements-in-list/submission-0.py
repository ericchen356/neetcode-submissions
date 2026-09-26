class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict = {}

        # frequency map for each number 

        for num in nums: 
            if num in dict: 
                dict[num] += 1 
            else: 
                dict[num] = 1

        buckets = [[] for i in range(len(nums) + 1)]

        for value, frequency in dict.items(): 
            buckets[frequency].append(value)
        
        results = []

        for frequency in range(len(buckets) - 1, 0, -1): 
            for num in buckets[frequency]: 
                results.append(num)

                if len(results) == k: 
                    return results

