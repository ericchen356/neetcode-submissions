class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = "".join(char.lower() for char in s if char.isalnum())

        left = 0 
        right = len(cleaned) - 1

        while left < (len(cleaned) / 2): 
            if cleaned[left] == cleaned[right]: 
                left += 1 
                right -= 1
            else: 
                return False

        return True