from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify_max(stones) 

        while len(stones) > 1:
            stone_1 = heappop_max(stones)
            stone_2 = heappop_max(stones)

            if stone_1 == stone_2:
                continue
            
            elif stone_1 > stone_2:
                stone_1 -= stone_2
                heappush_max(stones, stone_1)
            
            else:
                stone_2 -= stone_1
                heappush_max(stones, stone_2)

        if len(stones) == 1:
            return stones[0]
        return 0