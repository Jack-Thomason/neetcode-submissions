class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for val in row:
                if val == ".":
                    continue
                if val in seen:
                    return False    
                seen.add(val)
        
        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
            
        for b_r in range(0, 9, 3):
            for b_c in range(0, 9, 3):
                seen = set()

                for i in range(b_r, b_r + 3):
                    for j in range(b_c, b_c + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])

        return True 
