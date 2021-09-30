class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        new_tail = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[new_tail]:
                new_tail += 1
                nums[new_tail] = nums[i]
        return new_tail + 1


"""
Runtime: 80 ms, faster than 93.42% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.6 MB, less than 79.24% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""
