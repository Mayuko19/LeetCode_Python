class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i

""""
Runtime: 104 ms, faster than 7.21% of Python3 online submissions for Remove Duplicates from Sorted Array II.
Memory Usage: 14.2 MB, less than 61.14% of Python3 online submissions for Remove Duplicates from Sorted Array II.
""""
