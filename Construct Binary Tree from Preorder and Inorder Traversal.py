# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root 
####
Runtime: 235 ms, faster than 26.22% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 52.9 MB, less than 47.59% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
####
