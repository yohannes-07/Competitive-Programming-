class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # maximum distance passengers go with their car 
        passengers = [0] * (1001)
        
        # pick and drop passengers from start and at end
        # of each trip
        for no_of_passengers, start, end in trips:
            passengers[start] += no_of_passengers
            passengers[end] -= no_of_passengers
            
        max_passengers = 0
        
        # cumulative sum...if toatal passengers overpass the capacity
        # return false else return true
        for no_of_passengers in passengers:
            max_passengers +=  no_of_passengers
            if max_passengers > capacity:
                return False
        
        return True
        