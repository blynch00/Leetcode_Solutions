# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
# That is, each element of nums is covered by exactly one of the ranges, 
# and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        return_list = []
        index = 0
        # while index >= len(nums) - 1:
           


        return return_list
    

sol = Solution()
nums = [0,1,2,4,5,7] # ["0->2","4->5","7"]
print(sol.summaryRanges(nums))