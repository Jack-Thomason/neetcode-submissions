class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)] 

        for value, count in freq.items():
            bucket[count].append(value)

        
        res = []

        for freq in range(len(bucket) - 1, -1, -1):
            for i in bucket[freq]:
                res.append(i)
                if len(res) == k:
                    return res