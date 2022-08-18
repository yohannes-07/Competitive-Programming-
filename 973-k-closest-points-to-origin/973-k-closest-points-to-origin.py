class Solution:
    def kClosest(self, points, k):
        point=[[-i*i-j*j,i,j]for i,j in points[:k]]
        
        heapq.heapify(point)
        
        for x,y in points[k:]:
            dist=x*x+y*y
            
            if -point[0][0]>dist:
                heapq.heappush(point,[-dist,x,y])
                
                heapq.heappop(point)
        return[[x,y]for dist,x,y in point]