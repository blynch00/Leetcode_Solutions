class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # return arr where arr[i] = all previous values * all post values

        # previous_values = postfix
        prefix = [1] * len(nums)


        # post values = postfix
        postfix = [1] * len(nums)


        # Calculating every product at the given value
        for x in range(0, len(prefix)):
            if x == 0:
                continue
            prefix[x] = prefix[x-1] * nums[x-1]
        
        for x in reversed(range(0, len(postfix))):
            if x == len(postfix) - 1:
                continue
            postfix[x] = postfix[x+1] * nums[x+1]
        
        for x in range(0, len(nums)):
            prefix[x] =  prefix[x] * postfix[x]
        
        return prefix