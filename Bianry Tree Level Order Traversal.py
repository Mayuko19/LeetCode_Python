class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans, level = [], 0
        self.dfs(root, level, ans)
        return ans
    
    def dfs(self, root, level, ans):
        if not root:
            return 
        
        if len(ans) < level +1:
            ans.append([])
        ans[level].append(root.val)
        self.dfs(root.left, level+1, ans)
        self.dfs(root.right, level+1, ans)
        
""""
Runtime: 36 ms, faster than 67.28% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.7 MB, less than 25.50% of Python3 online submissions for Binary Tree Level Order Traversal.
""""
