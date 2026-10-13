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
        heapq.heapify(min_heap)
        res = 0
        intervals.sort(key = lambda x: x.start)
        for interval in intervals:
            start = interval.start
            end = interval.end
            if len(min_heap)==0:
                heapq.heappush(min_heap,(end,start))
                res +=1
            elif start < min_heap[0][0]:
                heapq.heappush(min_heap,(end,start))
                res = max(res,len(min_heap))
            else:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (end,start))

        return res