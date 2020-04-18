class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if len(grid) < 1:
            return 0
        
        def dfs (r,c):
            if r<0 or c<0 or r>=rows or c>=col or grid[r][c] == '0':
                return;
            grid[r][c] = '0'

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        rows = len(grid)
        col = len(grid[0])

        island = 0

        for i in range(rows):
            for j in range(col):

                if grid[i][j] == '1':
                    island += 1
                    dfs(i,j)
        return island
           
            
        