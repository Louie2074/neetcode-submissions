"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        min_heap = []
        intervals.sort(key = lambda x: x.start)
        for interval in intervals:
            start = interval.start
            end = interval.end
            if min_heap and start >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,end)
                

        return len(min_heap)