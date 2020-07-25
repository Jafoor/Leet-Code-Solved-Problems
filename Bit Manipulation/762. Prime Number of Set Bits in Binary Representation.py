from collections import Counter
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        
        primes = [2,3,5,7,11,13,17,19,23,29,31]
        ans = 0
        for i in range(L,R+1):
            x = bin(i).count('1')
            if x in primes:
                ans += 1
        return ans