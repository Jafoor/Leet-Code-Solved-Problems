class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i in range(0,len(nums)-1):
            if nums[i] == 0:
                if(mx<=i):
                    return False
            mx = max(mx, i+nums[i])
        return mx>=len(nums)-1
                
        