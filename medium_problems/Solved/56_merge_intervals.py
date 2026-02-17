class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # want to keep the array sorted, by starting values (we want to check sequentially)

        # Iterate through each sub-array, checking if previous stop < current_begin

        # Add full interval to list.
        ranges = []
        intervals.sort(key = lambda i: i[0])
        prev_start = -1
        prev_stop = -1
        for x in range(len(intervals)):
            start, stop = intervals[x]
            if x == 0:
                prev_start = start
                prev_stop = stop
                continue
            if prev_stop < start:
                ranges.append([prev_start,prev_stop])
                prev_start = start
                prev_stop = stop
                continue
            elif prev_start <= start and prev_stop <= stop:
                prev_stop = stop
                continue
        ranges.append([prev_start, prev_stop])
        return ranges