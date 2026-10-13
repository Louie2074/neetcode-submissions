class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])

        results = [intervals[0]]

        for start, end in intervals:
            if start < results[-1][1]:
                results[-1][1] = min(results[-1][1], end)
            else:
                results.append([start,end])
        return len(intervals) - len(results)