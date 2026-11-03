class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        r = max(piles)
        l = 1
        res = max(piles)

        while l <= r: 
            hour_count = 0 
            mid = (l + r) // 2
            for pile in piles: 
                if pile % mid != 0: 
                    hour_count += (pile // mid) + 1 
                else: 
                    hour_count += (pile // mid)
                
            if hour_count > h: 
                l = mid + 1
            elif hour_count <= h: 
                r = mid - 1
                res = min(res, mid)
        
        return res