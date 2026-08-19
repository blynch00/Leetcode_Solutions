from typing import *
from collections import *
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        unique_arr_1 = []
        unique_arr_2 = []

        nums1 = set(nums1)
        nums2 = set(nums2)

        for x in nums1:
            if x not in nums2:
                unique_arr_1.append(x)
        for y in nums2:
            if y not in nums1:
                unique_arr_2.append(y)
        return[unique_arr_1,unique_arr_2]
        
