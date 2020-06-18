class Solution:
    def dfs(self, board, i, j):
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j] != "O":
            return
        board[i][j] = 'T'
        n_list = [[i+1,j], [i-1,j], [i,j-1], [i, j+1]]
        for x,y in n_list:
            self.dfs(board, x, y)
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 0
        
        for i in range(0, len(board)):
            self.dfs(board, i, 0)
            self.dfs(board, i, len(board[0])-1)
            
        for j in range(0, len(board[0])):
            self.dfs(board, 0, j)
            self.dfs(board, len(board)-1, j)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "T":
                    board[i][j] = "X"
                else:
                    board[i][j] = "O"
        
