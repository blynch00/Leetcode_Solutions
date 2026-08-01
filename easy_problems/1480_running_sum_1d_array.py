class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum_list = []
        sum_total = 0
        for x in range(0, len(nums)):
            sum_total += nums[x]
            sum_list.append(sum_total)
        return sum_list
