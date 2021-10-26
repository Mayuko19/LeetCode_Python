class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        max_num = max(nums)
        for i in range(len(nums)):
            temp += nums[i]
            if temp >= 0:
                max_num = max(max_num,temp)
            else:
                temp = 0
        return max_num

####
Runtime: 1031 ms, faster than 12.16% of Python3 online submissions for Maximum Subarray.
Memory Usage: 28.7 MB, less than 35.98% of Python3 online submissions for Maximum Subarray.
####
