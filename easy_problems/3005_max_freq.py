from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        total_elements = 0
        arr = Counter(nums)
        count = max(arr.values())
        for x in arr:
            if arr[x] == count:
                total_elements += count
        return total_elements
