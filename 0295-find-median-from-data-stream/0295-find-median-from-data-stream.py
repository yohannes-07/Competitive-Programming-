class MedianFinder:

    def __init__(self):
        self.min = [] # for nums after the median elem
        self.max = [] # for  nums before or equal to  the median elem

    def addNum(self, num: int) -> None:
       
        if not self.max:
            heappush(self.max, -num)
            return
        
        if self.max and num >  -self.max[0]:
            heappush(self.min, num)
            
        else:
            heappush(self.max, -num)
            
        if len(self.max) - len(self.min) == 2:
            heappush(self.min, -heappop(self.max))   
         
        elif len(self.min) - len(self.max) == 2:
            heappush(self.max, -heappop(self.min))   
      
       

    def findMedian(self) -> float:
        
        if len(self.min) == len(self.max):
            return (self.min[0] + (-1 * self.max[0]))/2
        
        elif len(self.max) > len(self.min):
            return  -1 * self.max[0]
        
        elif len(self.max) < len(self.min):
            return  self.min[0]
        
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()