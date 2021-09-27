class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.upper() if i.isalnum()]
        return s == s[::-1]
        
