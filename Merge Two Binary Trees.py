# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        
        ans = TreeNode(root1.val + root2.val)
        ans.left = self.mergeTrees(root1.left, root2.left)
        ans.right = self.mergeTrees(root1.right, root2.right)
        
        return ans

#####
Runtime: 137 ms, faster than 18.88% of Python3 online submissions for Merge Two Binary Trees.
Memory Usage: 15.3 MB, less than 92.49% of Python3 online submissions for Merge Two Binary Trees.
#####
