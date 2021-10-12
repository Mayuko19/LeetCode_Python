class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(cur, left, num):
            if left == 0:
                ans.append(cur+[])
                return 
            for i in range(num, len(candidates)):
                if left - candidates[i] >= 0:
                    cur.append(candidates[i])
                    dfs(cur, left - candidates[i], i)
                    cur.pop()
        dfs([], target, 0)
        return ans
""""
Runtime: 52 ms, faster than 94.65% of Python3 online submissions for Combination Sum.
Memory Usage: 14.5 MB, less than 22.75% of Python3 online submissions for Combination Sum.
""""
