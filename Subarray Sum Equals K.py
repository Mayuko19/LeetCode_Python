import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        count = calc = 0
        for n in nums:
            calc += n
            dic[calc], count = dic[calc] + 1, count + dic[calc -k]
        return count

      
""""
Runtime: 480 ms, faster than 5.18% of Python3 online submissions for Subarray Sum Equals K.
Memory Usage: 18.5 MB, less than 8.55% of Python3 online submissions for Subarray Sum Equals K.
""""
