class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
""""
Runtime: 61 ms, faster than 5.55% of Python3 online submissions for Pow(x, n).
Memory Usage: 14.3 MB, less than 17.10% of Python3 online submissions for Pow(x, n).
""""
