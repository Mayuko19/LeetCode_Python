class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list, t_list = list(s), list(t)
        
        s_list.sort()
        t_list.sort()
        
        if s_list == t_list:
            return True
        else:
            False
        
