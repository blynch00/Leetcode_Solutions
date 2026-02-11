from typing import List
import collections
# Given an array nums, you can perform the following operation any number of times:

# Select the adjacent pair with the minimum sum in nums. 
# If multiple such pairs exist, choose the leftmost one.
# Replace the pair with their sum.
# Return the minimum number of operations needed to make the array non-decreasing.

# An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        total_operations = 0
        print(nums)
        while self.not_sorted(nums) == False:
            index1, index2 = self.select_minimum(nums)
            print(f"Appending {nums[index1] + nums[index2]}")
            new_value = nums[index1] + nums[index2]
            nums[index1] = new_value
            nums.pop(index2)
            total_operations += 1
            print(nums)
        return total_operations



    def not_sorted(self, nums:List[int]) -> bool:
        for x in range(1, len(nums)):
            if nums[x-1] > nums[x]:
                return False
        return True
    
    def select_minimum(self, nums: List[int]) -> tuple:
        '''
        Returns the tuple of indices that add to smallest
        '''
        return_index = (0,0)
        smallest = float('inf')
        for x in range(1, len(nums)):
            if x == len(nums) - 1:
                if (nums[x-1] + nums[x]) < smallest:
                    return_index = (x-1, x)
                    smallest = nums[x-1] + nums[x]
                    break
            else:
                if (nums[x-1] + nums[x]) < (nums[x] + nums[x+1]):
                    if nums[x-1] + nums[x] < smallest:
                        return_index = (x-1, x)
                        smallest = nums[x-1] + nums[x]
                else:
                    if nums[x+1] + nums[x] < smallest:
                        return_index = (x, x+1)
                        smallest = nums[x] + nums[x+1]
        print(f"Return Addresses: {return_index}")
        return return_index


sol = Solution()
arr = [3,-3,-2,2,2,0,3,0,1,0,3,-2]
print(sol.minimumPairRemoval(arr))