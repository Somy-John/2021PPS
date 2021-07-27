class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1: return True
        if n%4 != 0: return False
        while (n:=n/4)>3: pass
        if n!=1: return False
        else: return True