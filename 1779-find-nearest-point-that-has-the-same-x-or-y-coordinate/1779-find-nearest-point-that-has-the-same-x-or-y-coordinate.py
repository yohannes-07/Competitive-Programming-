class Solution(object):
    def nearestValidPoint(self, x, y, points):
        
        #initialize minimum index and miniimum distance maximum value
        min_idx = len(points)
        min_dist = "inf"
        
        for i, point in enumerate(points):
            
            #check if the given point is valid
            if point[0] == x or point[1] == y:
                
                #do Manhattan distance with the vald point
                dist = abs(point[0] - x) + abs(point[1] - y)
                
                #update the minimum index if shortest distance is found
                if dist < min_dist:
                    min_idx = i
                    min_dist = dist
        
        #if valid shortest distance is found return the point's index otherwise -1
        if min_idx != len(points):
            return min_idx
        return -1
            