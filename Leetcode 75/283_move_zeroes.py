class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize 2 pointers
        np, zp = 0,0
        # Find first non-zero element of array
        while np < len(nums) and nums[np] == 0:
                np += 1

        while np < len(nums):
            if np == zp:
                np += 1
                continue
            if nums[np] != 0 and nums[zp] == 0:
                nums[zp],nums[np] = nums[np], nums[zp]
                np += 1
                zp += 1
            elif nums[np] != 0 and nums[zp] != 0:
                zp += 1
            else:
                np += 1
        