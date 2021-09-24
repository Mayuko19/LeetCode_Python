class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    for num in nums:
      num_count = nums.count(num)
      if num_count == 1:
        return num
            
            
        
