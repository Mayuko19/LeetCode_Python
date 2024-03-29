class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        obstacleGrid[0][0] = 1
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        for i in range(1, m):
            obstacleGrid[i][0] = obstacleGrid[i-1][0]*(1-obstacleGrid[i][0]) 
            
        for j in range(1, n):
            obstacleGrid[0][j] = obstacleGrid[0][j-1]*(1-obstacleGrid[0][j])
            
        for i in range(1, m):
            for j in range(1, n):
                obstacleGrid[i][j] = (1-obstacleGrid[i][j])*(obstacleGrid[i-1][j] + obstacleGrid[i][j-1])
                
        return obstacleGrid[-1][-1]
####
Runtime: 44 ms, faster than 71.86% of Python3 online submissions for Unique Paths II.
Memory Usage: 14.4 MB, less than 60.79% of Python3 online submissions for Unique Paths II.
####
