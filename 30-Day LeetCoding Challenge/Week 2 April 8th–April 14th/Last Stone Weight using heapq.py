import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-i for i in stones]
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            
            stones1 = heapq.heappop(stones)
            stones2 = heapq.heappop(stones)
            
            if stones1 != stones2:
                heapq.heappush(stones,stones1-stones2)
        return -stones[-1] if stones else 0
            
            
        