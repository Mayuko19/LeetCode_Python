class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()

""""
Runtime: 100 ms, faster than 69.89% of Python3 online submissions for Group Anagrams.
Memory Usage: 18.2 MB, less than 29.41% of Python3 online submissions for Group Anagrams.
""""
