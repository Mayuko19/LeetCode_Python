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
                queue.append((curr.left, levle+1))
            if curr.right:
                queue.append((curr.right, level+1))
        return level
