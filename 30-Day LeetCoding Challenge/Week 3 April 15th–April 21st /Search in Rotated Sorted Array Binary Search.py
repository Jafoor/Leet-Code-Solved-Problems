class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        return solve(0,l-1,nums,target)
            
        

def solve(s,e,nums,key):
    while s<=e:
        m = (s+e)//2
        left = nums[s]
        right = nums[e]
        mid = nums[m]
        
        if mid == key:
            return m
        if mid < left:
            if key <= right and key > mid:
                s = m+1
            else:
                e = m-1
        elif mid > right:
            if key >= left and key < mid:
                e = m-1
            else:
                s = m+1
        else:
            if key > mid:
                s = m+1
            else:
                e = m-1
    return -1
            
        