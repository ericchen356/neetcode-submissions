class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): 
            return False

        dict = {} 

        for i in range(len(s)): 
            if s[i] not in dict: 
                dict[s[i]] = 0
            
            dict[s[i]] += 1 
            
            if t[i] not in dict: 
                dict[t[i]] = 0
            
            dict[t[i]] -= 1 
        
        for value in dict.values(): 
            if value != 0: 
                return False

        print(dict)

        return True