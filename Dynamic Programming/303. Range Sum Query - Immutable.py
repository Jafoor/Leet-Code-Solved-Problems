class NumArray:
    
    
    def __init__(self, nums: List[int]):
        if len(nums) == 0:
            return None
        self.sum1 = []
        self.sum1.append(nums[0])
        for i in range(1,len(nums)):
            self.sum1.append(self.sum1[i-1]+nums[i])
        self.nums = nums
    
    def sumRange(self, i: int, j: int) -> int:
        ans = self.sum1[j]
        if i == j:
            return self.nums[i]
        elif i !=0:
            ans -= self.sum1[i-1]
        
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)