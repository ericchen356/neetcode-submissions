class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        dict = {} 

        for word in strs: 
            key = [0] * 26
            for char in word: 
                key[ord(char) - ord('a')] += 1

            if tuple(key) not in dict: 
                dict[tuple(key)] = [word]
            else: 
                dict[tuple(key)].append(word)

        return list(dict.values())