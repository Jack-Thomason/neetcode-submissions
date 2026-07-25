class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])

        kept = 0
        previous_end = float("-inf")

        for start, end in intervals:
            if start >= previous_end:
                kept += 1
                previous_end = end

        return len(intervals) - kept

        