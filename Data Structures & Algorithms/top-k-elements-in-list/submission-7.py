class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        bucket = [[] for _ in range(len(nums)+1)]

        for value, count in freq.items():
            bucket[count].append(value)

        res = []

        for count in range(len(bucket) - 1, -1, -1):
            for n in bucket[count]:
                res.append(n)

                if len(res) == k:
                    return res