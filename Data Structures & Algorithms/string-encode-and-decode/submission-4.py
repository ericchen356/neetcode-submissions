class Solution:

    def encode(self, strs: List[str]) -> str:
        
        output = ""

        for word in strs: 
            output = output + str(len(word)) + "#" + word
    
        return output

    def decode(self, s: str) -> List[str]:

        result = []
        
        i = 0 

        length = 0
        while i < (len(s) - 1): 
            if s[i].isdigit():
                if length == 0: 
                    length = int(s[i])
                else: 
                    length = (length * 10) + int(s[i])

            i += 1 

            if s[i] == "#": 
                word = ""
                for j in range(1, length+1): 

                    word = word + s[i+j]

                result.append(word)
                
                i += length+1
                length = 0 
            

        return result 
