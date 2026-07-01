class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        final_arr = []
        nums.sort()
        i = 0

        while i < len(nums) - 2:
            low = i + 1
            high = len(nums) - 1

            while low < high:
                pos_sum = nums[i] + nums[low] + nums[high]
                if pos_sum < 0:
                    low += 1
                    continue

                elif pos_sum > 0:   
                    high -= 1
                    continue
                
                else:
                    # Otherwise the triple == 0, so we add the tuple
                    triple_pair = [nums[i], nums[low], nums[high]]
                    final_arr.append(triple_pair.copy())
                    l, h = nums[low], nums[high]
                    while nums[low] == l and l < h:
                        low += 1
                    if l >= h:
                        break
                    while nums[high] == h and h > l:
                        h -= 1
                    if h <= l:
                        break
            x = nums[i]
            while i < len(nums) and nums[i] == x:
                i += 1
        return final_arr