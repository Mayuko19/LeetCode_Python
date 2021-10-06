class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = []
        stack.append((root, targetSum-root.val))
        
        while stack:
            node, targetSum = stack.pop()
            if not node.left and not node.right and targetSum == 0:
                return True
            if node.left:
                stack.append((node.left, targetSum-node.left.val))
            if node.right:
                stack.append((node.right, targetSum-node.right.val))
        return False
      
""""
Runtime: 36 ms, faster than 95.79% of Python3 online submissions for Path Sum.
Memory Usage: 15.2 MB, less than 63.52% of Python3 online submissions for Path Sum.
""""
