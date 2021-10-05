from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            curr, level = queue.popleft()
            if curr.left:
                queue.append((curr.left, level+1))
            if curr.right:
                queue.append((curr.right, level+1))
        return level
""""
Runtime: 44 ms, faster than 56.41% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.3 MB, less than 89.26% of Python3 online submissions for Maximum Depth of Binary Tree.
""""
