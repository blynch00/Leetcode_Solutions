from typing import *
from collections import *
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        for x in range(0, len(gain)):
            if x == 0:
                continue
            gain[x] += gain[x-1]
        if max(gain) < 0:
            return 0
        return max(gain)