class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()
        while len(stones) >=2:
            x = stones[-1]
            y = stones[-2]
            if x == y:
                stones.pop()
                stones.pop()
            else:
                z = x-y
                stones.pop()
                stones.pop()
                stones.append(z)
                stones.sort()
            
        return stones[-1] if(len(stones)==1) else 0 
            
            
        