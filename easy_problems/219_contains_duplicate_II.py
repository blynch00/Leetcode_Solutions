#Given an integer array nums and an integer k, return true if there are 
# two distinct indices i and j in the array such that:
# 1) nums[i] == nums[j] 
# 2) abs(i - j) <= k.
# I.E. there are 2 matching integers that are, at most, K values apart within the array.


def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    if len(nums) == 1 or k == 0:
        return False
    seen = {}
    for x in range(len(nums)):
        if nums[x] not in seen:
            seen[nums[x]] = x
            continue
        else:
            #print(abs(x))
            #print(abs(seen[nums[x]]))
            if abs(x) - abs(seen[nums[x]])<= k:
                return True
            # Otherwise, set seen to new value
            seen[nums[x]] = x
    return False
