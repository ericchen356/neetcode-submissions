class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate list of prefix product
        # if n = 0, repeat same value from prev element 
        # in calcualting the vals, if hasZero = True -> every product is 0 
        # value = max product * [value of current value's index - 1] / [current value]
        # put all into hashmap 

        # have a flag for more than 2 zeroes, to return all zeros 

        prefixProduct = []

        zeros = 0

        for num in nums: 
            if not prefixProduct: 
                if num == 0: 
                    zeros += 1
                    prefixProduct.append(1)
                else: 
                    prefixProduct.append(num)
            else: 
                if num == 0: 
                    zeros += 1 
                    prefixProduct.append(prefixProduct[-1])
                else: 
                    prefixProduct.append(prefixProduct[-1] * num)

        results = []

        for i in range(len(nums)): 
            if nums[i] != 0:
                if zeros > 0: 
                    results.append(0)
                elif zeros == 0: 
                    if i == 0: 
                        results.append(int(prefixProduct[-1] / prefixProduct[i]))
                    else: 
                        results.append(int(prefixProduct[-1] * prefixProduct[i-1] / prefixProduct[i]))
            elif nums[i] == 0: 
                if zeros >= 2: 
                    results.append(0)
                else:
                    if i == 0: 
                        results.append(int(prefixProduct[-1] / prefixProduct[i]))
                    else: 
                        results.append(int(prefixProduct[-1] * prefixProduct[i-1] / prefixProduct[i]))

        return results