class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return l
      
""""
Runtime: 40 ms, faster than 98.27% of Python3 online submissions for Search Insert Position.
Memory Usage: 15.2 MB, less than 22.10% of Python3 online submissions for Search Insert Position.
""""
