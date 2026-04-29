from typing import List, Counter
from heapq import heappop_max as heappop, heappush_max as heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        top_elements = []
        max_heap = []
        for x in nums:
            heappush(max_heap, (nums[x],x))
        print(f"Nums: {nums}")
        for y in range(0, k):
            popped = heappop(max_heap)
            count, element = popped
            print(count, element)
            top_elements.append(element)
        return top_elements

sol = Solution()
arr = [1,1,1,2,2,3,6,6,6,6,6,6,6,6,6,6,6,6,6,2,2,2,2,2,2]
print(sol.topKFrequent(arr, 2))