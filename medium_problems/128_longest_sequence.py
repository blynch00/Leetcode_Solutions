from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        seen = set(nums)
        for x in seen:
            print(x)
        counters = -1
        count = 0
        last_element = None
        for x in seen:
            if x == nums[0]:
                count += 1
                last_element = x
                continue
            if x-1 == last_element

sol = Solution()
seq = [1,0,1,2]
print(sol.longestConsecutive(seq))