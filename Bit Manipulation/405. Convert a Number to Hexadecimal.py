class Solution:
    def toHex(self, num: int) -> str:
        
        if num == 0:
            return "0"
        if num < 0:
            num += 16 ** 8
        hexa = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        res = ""
        while num:
            
            num, res = num//16, hexa[num%16]+res
            
        return res