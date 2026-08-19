class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        max_num = arr[-1]
        curr_num = 1
        index = 0

        missing = []

        while len(missing) < k:
            if curr_num > max_num:
                missing.append(curr_num)
                curr_num += 1
                continue
            while curr_num != arr[index]:
                missing.append(curr_num)
                curr_num += 1
            index += 1
            curr_num += 1
        
        return missing[k-1]