class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2: 
            return []
        n  = len(nums2)
        res = []
        cnt = 0
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(len(nums1))]
        while heap and cnt < k:
            cnt += 1
            sm, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n: 
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res           
""""
Runtime: 669 ms, faster than 49.27% of Python3 online submissions for Find K Pairs with Smallest Sums.
Memory Usage: 36 MB, less than 19.10% of Python3 online submissions for Find K Pairs with Smallest Sums.
""""
