'''
Explanation

XOR operater: Sets each bit to 1 if only one of two bits is 1
1 ^ 7 = 6 -------> 1 ^ 111 = 110
6 ^ 13 = 11 -----> 110 ^ 1101 = 1011
1 ^ 7 ^ 13 = 11 ------> 1 ^ 111 ^ 1101 = 1011
if you want to get the result of 1 ^ 7 from 13 and 11, you can:
11 ^ 13 = 1 ^ 7 ^ 13 ^ 13 = 1 ^ 7 = 6 ------> 1 ^ 111 ^ 1101 ^ 1101 = 1 ^ 111 = 110
------------------------------------------------------(1101 ^ 1101 = 0)-------------
Iterate arr and accumulate XOR: total ^= arr[r]
Count positions in range (0, r): for l in range(r)
Found it: if temp == 0 and update results: res += r - l
Remove the left nums: temp ^= arr[l]

Complexity
Time: O(n^2)
Space: O(1)
'''

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        total = 0
        result = 0
        for i in range(len(arr)):
            total ^= arr[i]
            temp = total
            for j in range(i):
                if temp == 0:
                    result += (i-j)
                temp ^= arr[j]
        return result