class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum = 1
        zero = 0
        one = 0
        for i in nums:
            if i != 0:
                sum *= i
            if i == 0:
                zero += 1
            if i == 1:
                one += 1
        
        product = []
        p = sum
        for i in nums:
            if i==0 and zero == 1:
                p = sum
            elif zero>1:
                p = 0
            elif i != 0 and zero == 0:
                p = sum//i
            elif i != 0 and zero != 0:
                p = 0
            
                
            product.append(p)
        return product 
        