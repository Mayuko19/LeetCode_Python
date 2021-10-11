class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums, [], ans)
        return ans
        
    def dfs(self, nums, emp, ans):
        if not nums:
            ans.append(emp)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], emp+[nums[i]],ans)
""""
Runtime: 49 ms, faster than 32.72% of Python3 online submissions for Permutations.
Memory Usage: 14.3 MB, less than 69.54% of Python3 online submissions for Permutations.\\
""""
