from typing import *
from collections import *

class Solution:
    def tribonacci(self, n: int) -> int:
        # T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

        # Return value of T_n, given N.

        seen = {0:0, 1:1, 2:1}
        
        if n in seen:
            return seen[n]
        
        start = max(seen)
        for x in range(start,n+1):
            if x not in seen:
                seen[x] = seen[x-1]+seen[x-2]+seen[x-3]
                print(f"{x}:{seen[x]}")
        return seen[n]
        

sol = Solution()
print(sol.tribonacci(5))