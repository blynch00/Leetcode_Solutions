from collections import Counter
from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # for any position x in nums:
        # target = k - nums[x]

        # Use dict to track pairs and indices, removing them and continuing
        if len(nums) == 1:
            return 0
        
        total_pairs = 0

        arr = Counter(nums)

        for x in arr:
            target = k - x
            if target not in arr:
                continue
            # Since we know it is part of the set:
            if x == target:
                if arr[x] < 2:
                    continue
                else:
                    while arr[x] >=2:
                        arr[x] -= 2
                        total_pairs += 1
                    continue
            if arr[target] < 0:
                continue
            else:
                while arr[target] >= 1 and arr[x] >= 1:
                    arr[target] -= 1
                    arr[x] -=1
                    total_pairs += 1
                continue
        return total_pairs

                    
         
    