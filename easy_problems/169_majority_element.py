from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = len(nums) // 2
        nums = Counter(nums)
        for x in nums:
            if nums[x] > count:
                return x
