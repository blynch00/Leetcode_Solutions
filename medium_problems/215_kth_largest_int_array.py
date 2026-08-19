class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        nums.sort(reverse=True)
        return nums[k-1]
