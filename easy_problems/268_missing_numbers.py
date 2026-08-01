class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Brute Force: .sort(), then iterate through list to find the missing number
            # O(n log n) time complexity
        
        # Heap: call heapq.heapify(nums) to make a min heap, then:
            # 1. check if first number is 0, if not return 0
        heapq.heapify(nums)
        least = heapq.heappop(nums)
        if least != 0:
            return 0
        prev = least
        while len(nums) > 0:
            n = heapq.heappop(nums)
            if prev + 1 != n:
                # This is the missing number
                return prev + 1
            else:
                prev = n 
                continue
        
        return prev + 1
            # track previous, then while heap, pop and compare prev +1 == current:
                # if uneven, return prev + 1
                # if even, prev = current, continue
            
            # If prev == current, return current + 1;
            # Missing number is N
