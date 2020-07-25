class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        count = 0
        while a or b or c:
        
            if ((a&1 | b&1) == 0 and c&1 == 1):
                count += 1
            elif (a&1 | b&1) == 1 and c&1 == 0:
                count += (a&1) + (b&1)
                
            a >>= 1
            b >>= 1
            c >>= 1
        return count