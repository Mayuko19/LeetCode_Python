class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) //2
        
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        if mid < len(nums)-1:
            root.right = self.sortedArrayToBST(nums[mid+1:])
        return root 
""""
Runtime: 52 ms, faster than 97.18% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.6 MB, less than 86.92% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
""""
