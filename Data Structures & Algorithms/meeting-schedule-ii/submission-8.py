"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)

        max_rooms = 0
        active = []
        for interval in intervals:
            while active and interval.start >= active[0]:
                    heapq.heappop(active)

            heapq.heappush(active, interval.end)
            max_rooms = max(max_rooms, len(active))

        return max_rooms
            
