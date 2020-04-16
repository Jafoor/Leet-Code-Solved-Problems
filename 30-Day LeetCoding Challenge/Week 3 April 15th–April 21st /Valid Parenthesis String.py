class Solution:
    def checkValidString(self, s: str) -> bool:
        suru = shes = 0
        l = len(s)
        for i in range(0,l):
            if s[i] == '(' or s[i] == '*':
                suru += 1
            else:
                suru -= 1
            if s[l-1-i] == ')' or s[l-1-i] == '*':
                shes += 1
            else:
                shes -= 1
            if suru<0 or shes<0:
                return False
        return True
            
          
            
            
        
        