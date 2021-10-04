class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None:
            return None
        
        for i in range(len(nums)):
            mid = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == mid:
                    return i, j

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[target-nums[i]] = i 
            else:
                return hashmap[nums[i]], i                
                
""""
Runtime: 112 ms, faster than 42.51% of Python3 online submissions for Two Sum.
Memory Usage: 15.6 MB, less than 8.99% of Python3 online submissions for Two Sum
""""

