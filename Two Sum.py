class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None:
            return None
        
        for i in range(len(nums)):
            mid = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == mid:
                    return i, j

