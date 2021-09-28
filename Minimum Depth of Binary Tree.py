class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))

"""
Runtime: 480 ms, faster than 86.58% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 49 MB, less than 94.65% of Python3 online submissions for Minimum Depth of Binary Tree.
"""
