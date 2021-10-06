class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low, high = float('-inf'), float('inf')
        def helper(node, low, high):
            if not node:
                return True
            val = node.val
            if val <= low or val >= high:
                return False
            if not helper(node.left, low, val):
                return False
            if not helper(node.right, val, high):
                return False
            return True
        return helper(root, low, high)
            
""""
Runtime: 53 ms, faster than 31.59% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.4 MB, less than 80.79% of Python3 online submissions for Validate Binary Search Tree.
""""
