from typing import List
def singleNumber(nums: List[int]) -> int:
    #Given a non-empty array of integers nums, every element appears twice
    #except for one. Find that single one.
    index = 0
    for num in nums:
        index ^= num
    return index

nums = [1,2,3,1,2,3,4]
print(singleNumber(nums))