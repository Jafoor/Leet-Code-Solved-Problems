class Solution:
    def isHappy(self, n : int) -> bool:
        
        i = 0
        while n != 1 and i<50:
            p = 0
            while n>0:
                p += (n%10)**2
                n//=10
                i += 1
            n = p
        return n==1