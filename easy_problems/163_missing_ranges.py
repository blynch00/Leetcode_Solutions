
class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        if len(nums) == 0:
            return [[lower, upper]]
        # 2 pointers
        p1 = 0
        # Create return array
        return_arr = []
        
        # Check for min(lower, p1) in array
        if (lower < nums[p1]):
            return_arr.append([lower, nums[p1] - 1])
        else:
            # if nums[p1] < lower, we move p1 up until lower < nums[p1]
            while (p1 < len(nums) and lower > nums[p1]):
                p1 += 1
            if (p1 == len(nums)):
                return [[lower, upper]]
            if (lower < nums[p1]):
                # If there is a gap between lower and nums[p1], add it
                return_arr.append([lower, nums[p1]-1])
        
        while (p1 < len(nums)):
            if (p1 +1 == len(nums)):
                if (upper > nums[p1]):
                    return_arr.append([nums[p1] + 1, upper])
                return return_arr
            
            while (p1 < len(nums)- 1 and nums[p1 + 1] == nums[p1] + 1): 
                p1 += 1

            if (p1 == len(nums)- 1):
                # We have gotten to the end
                if (upper > nums[p1]):
                    return_arr.append([nums[p1] + 1, upper])
                    return return_arr
                elif (upper <= nums[p1]): return return_arr
            
            else:
                # Otherwise we have a gap
                return_arr.append([nums[p1] + 1, nums[p1 + 1] - 1])
                p1+= 1
                
                
                

        
        
        return return_arr
