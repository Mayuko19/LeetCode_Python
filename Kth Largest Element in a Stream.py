import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.lists = []
        self.num = k
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        heapq.heappush(self.lists, val)
        if len(self.lists) > self.num:
            heapq.heappop(self.lists)
        return self.lists[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
####
Runtime: 100 ms, faster than 72.72% of Python3 online submissions for Kth Largest Element in a Stream.
Memory Usage: 18.2 MB, less than 93.52% of Python3 online submissions for Kth Largest Element in a Stream.
####
