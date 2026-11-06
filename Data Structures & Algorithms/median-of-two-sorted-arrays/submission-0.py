class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # let arr1 be the shortest 
        if len(nums1) < len(nums2): 
            arr1 = nums1
            arr2 = nums2
        else: 
            arr1 = nums2
            arr2 = nums1
        
        total = len(nums1) + len(nums2)
        half = (total) // 2 
        
        l = 0 
        r = len(arr1) - 1 

        while True: 
            i = (l + r) // 2 # index of left partition of arr1 
            j = half - i - 2 # index of left partition of arr2

            left1 = arr1[i] if i >= 0 else float("-inf")
            left2 = arr2[j] if j >= 0 else float("-inf")
            right2 = arr2[j + 1] if j + 1 < len(arr2) else float("inf")
            right1 = arr1[i + 1] if i + 1 < len(arr1) else float("inf")

            if left2 > right1: 
                l = i + 1
            elif left1 > right2: 
                r = i - 1
            else: 
                if total % 2 == 0: 
                    return (max(left1, left2) + min(right2, right1)) / 2
                else: 
                    return min(right2, right1)