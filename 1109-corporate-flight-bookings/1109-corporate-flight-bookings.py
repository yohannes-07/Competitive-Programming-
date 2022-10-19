class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (n)
        for row in bookings:
            res[row[0]-1] += row[2]
            
            if row[1] < n:
                res[row[1]] += -row[2]
                
           
        for i in range(1, n):
            res[i] += res[i-1]
            
        return res
                         