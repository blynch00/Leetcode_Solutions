# integer array nums:
    # nums.length == 2 * n
    # nums contains n + 1 unique elements.
    # Exactly one element of nums is repeated n times.

# Return the element that is repeated n times.

def repeatedNTimes(nums: list[int]) -> int:
    seen = {}
    for element in nums:
        if element in seen:
            seen[element] += 1
            if seen[element] == len(nums) // 2:
                return element
        else:
            seen[element] = 1
    return seen


nums = [1,2,3,3]
print(repeatedNTimes(nums))