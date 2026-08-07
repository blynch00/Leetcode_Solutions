from typing import List
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        # can only have 1 processor, checks edge case
        if len(processorTime) == 1:
            return max(processorTime) + max(tasks)
        
        longest_time = 0
        # Min time: Largest tasks assigned to the earliest core, meaning tasks 1-4 to processor 1, 5-8 to 2, etc.
        # Sort processors to be the fastest
        processorTime.sort(reverse=False)
        # Sort tasks by slowest
        tasks.sort(reverse=False)
        for x in processorTime:
            m = 0
            # Pop 4 tasks, keeping the largest value
            for y in range(0, 4):
                m = max(m, tasks.pop())
            # Longest time = slowest of core + times used.
            longest_time = max(longest_time, m + x)

        return longest_time
