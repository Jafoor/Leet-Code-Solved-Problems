class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pre1 = nums[0]
        pre2 = 0
        for i in range(1,len(nums)):
            pre2 = max(pre1,pre2+nums[i])
            pre1 = pre1 ^ pre2
            pre2 = pre1 ^ pre2
            pre1 = pre1 ^ pre2
        return pre1