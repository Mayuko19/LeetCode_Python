class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = nums[:k]
        heapq.heapify(pq)
        for x in nums[k:]:
            heapq.heappush(pq, x)
            heapq.heappop(pq)
        return pq[0]

""""
Runtime: 56 ms, faster than 97.28% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 15.1 MB, less than 47.10% of Python3 online submissions for Kth Largest Element in an Array.
""""
