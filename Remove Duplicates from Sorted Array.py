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

if __name__ == '__main__':
    instance = Solution()
    print(instance.removeDuplicates([1,1,2,2,3,3,3,4,4,5,5,]))
