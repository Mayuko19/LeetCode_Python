class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.dfs(n,n,"",ans)
        return ans

    def dfs(self,left,right,path,ans):
        if left > right or left < 0 or right < 0:
            return 
        if left == 0 and right == 0:
            ans.append(path)
            return
        self.dfs(left-1,right,path+'(',ans)
        self.dfs(left,right-1,path+')',ans)
""""
Runtime: 43 ms, faster than 38.16% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.7 MB, less than 11.34% of Python3 online submissions for Generate Parentheses.
""""
