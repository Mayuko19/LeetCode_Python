class Solution:
    def reverse(self, x: int) -> int:
        max = 2 ** 31 -1
        if abs(x) > max:
            return 0
        
        if x < 0:
            reverse_int = -int(str(abs(x))[::-1])
            
        else:
            reverse_int = int(str(abs(x))[::-1])
            
        
        if abs(reverse_int) > max:
            return 0
        else:
            return reverse_int
