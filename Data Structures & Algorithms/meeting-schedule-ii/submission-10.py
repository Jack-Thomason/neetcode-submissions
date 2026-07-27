"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)

        str_ptr = 0
        end_ptr = 0
        max_rooms = 0
        active = 0

        while str_ptr < len(intervals):
            if starts[str_ptr] < ends[end_ptr]:
                active += 1
                max_rooms = max(max_rooms, active)
                str_ptr += 1

            else:
                active -= 1
                end_ptr += 1
            
        return max_rooms
