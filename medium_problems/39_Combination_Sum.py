class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        solution_list = []
        candidates.sort()
        def backtrack_helper(running_total = 0, current_arr=[], index=0):
            # Start by checking for completion
            if running_total == target:
                solution_list.append(current_arr.copy())
                return
            # If the number is larger, we know we can't use this value again
            elif running_total > target:
                return
            
            # Check if the value would be larger than the total, if the current number is added
            if running_total + candidates[index] > target:
                return
            
            for num in range(index, len(candidates)):
                current_arr.append(candidates[num])
                running_total += candidates[num]
                backtrack_helper(running_total, current_arr, num)
                running_total -= candidates[num]
                current_arr.pop()
        
        arr = []
        run_total = 0
        backtrack_helper(run_total,arr, 0)
        return solution_list
            