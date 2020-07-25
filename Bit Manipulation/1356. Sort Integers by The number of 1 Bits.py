from collections import Counter
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        return sorted(arr, key = lambda num: (sum((num>>i)&1 for i in range(32)), num))

        '''
        return sorted(arr, key = lambda num: [bin(num).count('1'),num])
        '''