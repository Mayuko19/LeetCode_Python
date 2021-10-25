class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
            
        area, count = 0, 0
        
        def dfs(i, j):
            nonlocal count
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] != 1:
                return count
            if grid[i][j] == 1:
                count += 1
            
            grid[i][j] = '#'
            dfs(i+1, j) 
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs(i, j)
                area = max(count, area)
                count = 0
        
        return area
      
#####
Runtime: 265 ms, faster than 9.85% of Python3 online submissions for Max Area of Island.
Memory Usage: 17 MB, less than 37.80% of Python3 online submissions for Max Area of Island.
#####
