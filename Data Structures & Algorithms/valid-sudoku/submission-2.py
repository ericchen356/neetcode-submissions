class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check horizontals 

        for row in board: 
            freq = {}

            for col in row: 
                if col in freq: 
                    if col != ".":
                        return False
                else: 
                    freq[col] = 1
                    
        # check verticals 

        for col in range(9): 
            freq = {}
            for row in range(9): 
                if board[row][col] in freq: 
                    if board[row][col] != ".": 
                        return False
                else: 
                    freq[board[row][col]] = 1
             
        # check 3x3s 

        for i in range(0, 7, 3): 
            for j in range(0, 7, 3): 
                freq = {}
                for col in range(3):
                    for row in range(3): 
                        if board[row+i][col+j] in freq: 
                            if board[row+i][col+j] != ".": 
                                return False
                        else: 
                            freq[board[row+i][col+j]] = 1

        return True