class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr.sort()
        n = len(self.arr) - 1
        if((n+1) % 2 != 0):
            mid = int(n/2)
            return self.arr[mid]
        else:
            mid = int(n/2)
            right = mid+1
            left = mid
            
            return (self.arr[left] + self.arr[right])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()