from collections import Counter
class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        #with arr all being distinct, find all pairs of elements with the minimum absolute difference of any two elements.
        # pair [a,b] must both be in arr, where a < b and b - a = min ab difference
        arr.sort()
        min_diff = 0
        index = 0
        final_list = []
        while index != len(arr) - 1:
            if min_diff == 0:
                min_diff = abs(arr[index] - arr[index + 1])
            # print(f"Currently: {arr[index]} - {arr[index + 1]}")
            if abs(arr[index] - arr[index + 1]) < min_diff:
                min_diff = abs(arr[index] - arr[index + 1])
            index +=1 
        #print(f"min_diff: {min_diff}")  
        # Could save time if you check the minimum at the same time in which you iterate through
        for x in range(0, len(arr)-1):
                #print(arr[x], arr[y])
                if abs(arr[x] - arr[x + 1]) == min_diff:
                        final_list.append([arr[x],arr[x + 1]])
        return(final_list)

sol = Solution()
arr_1 = [4,2,1,3] # returns [[1,2],[2,3],[3,4]]
print(sol.minimumAbsDifference(arr_1))