class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda interval: interval[0])

        sorted_queries = sorted(
            (query, index)
            for index, query in enumerate(queries)
        )

        res = [-1] * len(queries)
        heap = []
        interval_index = 0

        for query, index in sorted_queries:
            while (
                interval_index < len(intervals)
                and intervals[interval_index][0] <= query
                ):
                left, right = intervals[interval_index]
                length = right - left + 1

                heapq.heappush(heap, (length, right))
                interval_index += 1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            if heap:
                res[index] = heap[0][0]
        
        return res

            