class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.averageTime = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)
    
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkedInStation, checkedInTime = self.checkin[id]
        currTime = t - checkedInTime
        
        if (checkedInStation, stationName) in self.averageTime:
            prevTime, count = self.averageTime[(checkedInStation, stationName)]
            avgTime = (prevTime * count + currTime) / (count + 1)
            self.averageTime[(checkedInStation, stationName)] = (avgTime, count + 1)
            
        else:
        
            self.averageTime[(checkedInStation, stationName)]  = (currTime,1)
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.averageTime[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)