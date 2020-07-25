'''
Approach 1: Cascading
Intuition

Let's start from empty subset in output list. At each step one takes new integer into consideration and generates new subsets from the existing ones.

Image
https://leetcode.com/problems/subsets/Figures/78/recursion.png
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ans = [[]]
        
        for num in nums:
            ans += [cur + [num] for cur in ans]
        return ans
            
'''
Using bitmasking. 
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        output = []
        for i in range(2**n, 2**(n+1)):
            bitmask = bin(i)[3:]
            output.append([nums[j] for j in range(n) if bitmask[j] =='1'])
        return output