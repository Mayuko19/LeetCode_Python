class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)

        pre = 0
        for curr in range(1, len(nums)):
            if nums[curr] != nums[pre]:
                pre += 1
                nums[pre] = nums[curr]
        return pre + 1
