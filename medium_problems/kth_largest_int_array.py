class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        nums.sort(key=int, reverse=True)
        return nums[k-1]

sol = Solution()
nums = ["3","6","7","10"]
k = 4
# Should return "3"
print(sol.kthLargestNumber(nums, k))
