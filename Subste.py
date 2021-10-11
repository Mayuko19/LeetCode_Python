class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(temp, end):
            ans.append(temp+[])
            if len(nums) == len(temp):
                return 
            for i in nums:
                if i > end:
                    temp.append(i)
                    dfs(temp, i)
                    temp.pop()
        dfs([], float(-inf))
        return ans
""""
Runtime: 48 ms, faster than 24.97% of Python3 online submissions for Subsets.
Memory Usage: 14.4 MB, less than 50.23% of Python3 online submissions for Subsets.
""""
