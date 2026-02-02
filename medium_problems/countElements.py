class Solution:
    def countElements(self, nums: list[int], k: int) -> int:

        return Solution.count_helper(self, nums,k, len(nums)-1)
    
    def count_helper(self, nums:list[int], k:int, count:int) -> int:
        total_count = 0
        if count < 0:
            return 0
        
        for x in range(len(nums)):
            if nums[x] > nums[count]:
                total_count += 1
        if total_count >= k:
            return 1 + Solution.count_helper(self, nums, k, count - 1)
        else:
            return Solution.count_helper(self, nums, k, count - 1)

sol = Solution()
nums = ["3","6","7","10"]
k = 4 # Returns 2
print(sol.countElements(nums, k))