class MedianFinder:

    def __init__(self):
        self.leftMaxHeap = []
        self.rightMinHeap = []
        self.res = []

        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftMaxHeap, -num)

        temp = -heapq.heappop(self.leftMaxHeap)
        heapq.heappush(self.rightMinHeap, temp)

        if len(self.rightMinHeap) > len(self.leftMaxHeap):
            temp = heapq.heappop(self.rightMinHeap)
            heapq.heappush(self.leftMaxHeap, -temp)


        

    def findMedian(self) -> float:
        median = 0.0
        if len(self.leftMaxHeap) != len(self.rightMinHeap):
            median = -self.leftMaxHeap[0]
        else:
            median = (-self.leftMaxHeap[0] + self.rightMinHeap[0]) / 2.0
        


        return median

        
        