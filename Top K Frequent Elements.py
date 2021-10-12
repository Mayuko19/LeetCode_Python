class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        key = count.get
        return heapq.nlargest(k, count.keys(), key)
      
""""
Runtime: 108 ms, faster than 48.85% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.6 MB, less than 83.74% of Python3 online submissions for Top K Frequent Elements.
""""
