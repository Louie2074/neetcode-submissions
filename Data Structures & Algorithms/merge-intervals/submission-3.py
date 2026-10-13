class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        result = []
        currentStart = intervals[0][0]
        currentEnd = intervals[0][1]

        for interval in intervals:
            if interval[0] <= currentEnd:
                currentEnd = max(interval[1], currentEnd)
            else:
                result.append([currentStart, currentEnd])
                currentStart = interval[0]
                currentEnd = interval[1]

        result.append([currentStart, currentEnd])
        return result

