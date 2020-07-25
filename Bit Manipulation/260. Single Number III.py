from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
       
        res = []
        count = Counter(nums)
        for i in count:
            if count[i] == 1:
                res.append(i)
        return res