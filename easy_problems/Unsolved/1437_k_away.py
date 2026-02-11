from typing import List
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        index = 0

        while index < len(nums):
            if nums[index] == 1:
                counter = 0
                index += 1
                if index == len(nums):
                    return True
                while index < len(nums) and nums[index] != 1:
                    counter += 1
                    index += 1
                if index == len(nums):
                    return True
                if counter < k:
                    return False
            else:
                index += 1

        return True

sol = Solution()
arr = [1,0,0,0,1,0,0,1,0]
print(sol.kLengthApart(arr,2))