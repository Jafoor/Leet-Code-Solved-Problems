class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        return solve(nums, 0, len(nums)-1)
    
def subarray(nums, l, m, h):
        
        sum = 0
        left = -100000
        for i in range(m, l-1, -1):
            sum += nums[i]
            
            if sum>left:
                left = sum
        
        sum = 0
        right = 0
        for i in range(m+1, h+1):
            sum += nums[i]
            
            if sum>right:
                right = sum
        
        return right+left
        
        
def solve (nums,l,h):
    if l==h:
        return nums[l]
    m = (l+h)//2

    return max(solve(nums,l,m),solve(nums,m+1,h),subarray(nums,l,m,h))
    
    
        
    
        
        