class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        for i,st in enumerate(s):
            if (st == 'V' or st == 'X') and i != 0 and s[i-1] == 'I':
                ans -= values[s[i-1]]
                ans += values[s[i-1:i+1]]
            elif (st == 'L' or st == 'C') and i != 0 and s[i-1] == 'X':
                ans -= values[s[i-1]]
                ans += values[s[i-1:i+1]]
            elif (st == 'D' or st == 'M') and i != 0 and s[i-1] == 'C':
                ans -= values[s[i-1]]
                ans += values[s[i-1:i+1]]
            else:
                ans += values[st]
            # print(ans)
        return ans
            
        
