from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_2 =[]
        for i in range(0, k):
            nums_2.append(nums[len(nums)-k+i])
            nums.pop(len(nums)-k+i)
        nums[:] = nums_2 + nums

        
        
        
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
