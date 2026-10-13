class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        results = [intervals[0]]

        for start, end in intervals:
            if start <= results[-1][1]:
                results[-1][1] = max(results[-1][1], end)
            else:
                results.append([start, end])
        return results