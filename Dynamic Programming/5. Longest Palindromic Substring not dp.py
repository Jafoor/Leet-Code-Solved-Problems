class Solution:
    def longestPalindrome(self, s: str) -> str:
        mx = 0
        n = len(s)
        strat = 0
        if not s:
            return s
        for i in range(n):
            
            k = i
            l = i
            while k+1<n and s[k] == s[k+1]:
                k+=1
            
            while l-1>=0 and k+1<n and s[k+1] == s[l-1]:
                k += 1
                l -= 1
            #print(k-l+1)
            if mx < (k-l+1):
                mx = k-l+1
                start = l
        #print(mx)
        return s[start:start+mx]
                
        