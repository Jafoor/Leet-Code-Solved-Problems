class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        i = 0
        while i<n:
            result ^= (start+i*2)
            i += 1
        return result