class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]

        for value, count in freq.items():
            bucket[count].append(value)

        res = []

        for count in range(len(bucket) - 1, 0 , -1):
            for num in bucket[count]:
                res.append(num)

                if len(res) == k:
                    return res
            