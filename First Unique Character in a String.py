class Solution:
    def firstUniqChar(self, s: str) -> int:
        count =  collections.Counter(s)
        print(count)
        for index, word in enumerate(s):
            if count[word] == 1:
                return index
            
        return -1
      
"""""
Runtime: 158 ms, faster than 37.33% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.6 MB, less than 8.85% of Python3 online submissions for First Unique Character in a String.
"""""
