class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        for i in range(1,len(arr),1):
            arr[i] ^= arr[i-1]
        ans = []

        for i,j in queries:
            if i != 0:
                answer = arr[j]^arr[i-1]
            else:
                answer = arr[j]
            ans.append(answer)
        return ans

        '''
        In one line
        return [ arr[i-1] ^ arr[j] if i else arr[j] for i, j in queries ]
        '''