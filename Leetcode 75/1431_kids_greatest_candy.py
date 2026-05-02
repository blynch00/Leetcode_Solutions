from typing import *
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Sort original array in n log n time
        new_candies = sorted(candies, reverse=True)
        # Create new array of len(candies)
        final_arr = [] 
        largest = new_candies[0]

        for x in range(0, len(candies)):
            if candies[x] + extraCandies >= largest:
                final_arr.append(True)
            else:
                final_arr.append(False)
        return final_arr

