
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        index = 1
        return_arr = []
        start_string = f"{nums[0]}->"
        print(f"start_string: {start_string}")

        while index != len(nums):
            if nums[index] == nums[index - 1] + 1:
                start_string += f"{nums[index]}->"
            elif nums[index] == nums[index - 1]:
                index += 1
                continue
            else:
                return_arr.append(start_string)
                start_string = ""
            index += 1
        return return_arr
