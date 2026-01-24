nums = [0,0,1,1,1,2,2,3,3,4]
#----------------------------
def removeDuplicates(self, nums: list[int]) -> int:
    total_seen = set()
    pointer_1 = 0
    pointer_2 = 0
    index = 0

    while index < len(nums):

        if index == 0:
            total_seen.add(nums[index])

        while pointer_2 <= len(nums) -1 and nums[pointer_1] == nums[pointer_2]:
            pointer_2 += 1
            
        if pointer_2 == len(nums) -1 and nums[pointer_2] in total_seen:
            return len(total_seen)
        index += 1
        











print(len(total_seen))