class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        temp = [] 
        stack = [root]
        flag = 1
        while stack:
            for i in range(len(stack)):
                node=stack.pop(0)
                temp+=[node.val]
                if node.left:
                    stack+=[node.left]
                if node.right:
                    stack+=[node.right]
            res+=[temp[::flag]]
            temp=[]
            flag*=-1
        return res
####
Runtime: 69 ms, faster than 5.59% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 14.5 MB, less than 72.02% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
####
