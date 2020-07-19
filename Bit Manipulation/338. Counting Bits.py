class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = []
        for i in range(num+1):
            j = i
            cnt = int(0)
            while j:
                if j & 1:
                    cnt += 1
                j = j >> 1
            ans.append(cnt)
        return ans