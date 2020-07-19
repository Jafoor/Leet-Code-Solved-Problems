class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        first = n%2
        n = n//2
        while n!= 0:
            print(first)
            if n%2 == first:
                return False
            else:
                first = n%2
                n = n//2
        return True