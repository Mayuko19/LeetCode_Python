class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        if n < m:
            self.uniquePaths(n, m)
            
        dp = [1]*n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]
""""
Runtime: 32 ms, faster than 71.45% of Python3 online submissions for Unique Paths.
Memory Usage: 14.3 MB, less than 65.68% of Python3 online submissions for Unique Paths.
""""
