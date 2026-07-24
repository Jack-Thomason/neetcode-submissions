class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        new_start, new_end = newInterval

        for i, (start, end) in enumerate(intervals):
            # interval completely before
            if new_start > end:
                result.append([start, end])

            # interval completely after
            elif start > new_end:
                result.append([new_start, new_end])
                result.extend(intervals[i:])
                return result

            # intervals overlap
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)

        # newInterval at end
        result.append([new_start, new_end])
        return result
        