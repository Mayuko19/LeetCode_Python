class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
            
        return stack == []
"""
Runtime: 39 ms, faster than 31.27% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.2 MB, less than 86.25% of Python3 online submissions for Valid Parentheses.
"""
