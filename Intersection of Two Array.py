class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)
        return list(set1&set2)
""""
Runtime: 40 ms, faster than 93.81% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.5 MB, less than 44.97% of Python3 online submissions for Intersection of Two Arrays.
""""
