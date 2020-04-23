class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        c = 0

        dic = {}
        for i in range(len(nums)):
            s += nums[i]
            if s==k:
                c += 1
            if s-k in dic:
                c += dic.get(s-k)
            dic[s] = dic.get(s,0) + 1
        return c
            
            
            
        