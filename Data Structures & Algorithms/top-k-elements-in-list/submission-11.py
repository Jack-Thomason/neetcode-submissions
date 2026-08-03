class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        heap = []
        for (value, count) in counts.items():
            heapq.heappush(heap,  (count, value))
            if len(heap) > k:
                heapq.heappop(heap)
            
        return [value for count, value in heap]
            

        