class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq = {}

        for char in s1:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        for i in range(len(s1)):
            if s2[i] in freq:
                freq[s2[i]] -= 1

        if all(value == 0 for value in freq.values()):
            return True

        left = 0

        for right in range(len(s1), len(s2)):
            if s2[right] in freq:
                freq[s2[right]] -= 1

            if s2[left] in freq:
                freq[s2[left]] += 1

            left += 1

            if all(value == 0 for value in freq.values()):
                return True

        return False