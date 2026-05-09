from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # return case if len = 2
        if len(height) == 2:
            return min(height)
        max_container = 0
        # Initialize at different ends; begin with the largest number possible, and only checking what could be larger (replacing the smaller number)
        left = 0
        right = len(height) - 1

        # While the pointers are not at the same number:
        while left <= right:
        
            # Calculate container size; smallest wall x distance between both
            container_size = min(height[left], height[right]) * (right - left)
            if container_size > max_container:
                max_container = container_size
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_container
