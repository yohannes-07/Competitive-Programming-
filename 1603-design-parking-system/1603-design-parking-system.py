class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.carTypes = [big, medium , small ]

    def addCar(self, carType):
        self.carTypes[carType - 1] -= 1
        if self.carTypes[carType - 1] < 0:
            
            return False
        return True 
         


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)