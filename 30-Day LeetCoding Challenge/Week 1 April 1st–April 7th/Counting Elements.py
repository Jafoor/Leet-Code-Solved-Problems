class Solution:
    def countElements(self, arr: List[int]) -> int:
        dict = {}
        for i in arr:
            dict[i] = i
        result = 0
        for i in arr:
            if i+1 in dict:
                result += 1
        return result
                
        
            