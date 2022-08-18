class Solution:
    def kClosest(self, points, k):
        pq=[[-i*i-j*j,i,j]for i,j in points[:k]]
        
        heapq.heapify(pq)
        
        for x,y in points[k:]:
            d=x*x+y*y
            
            if -pq[0][0]>d:
                heapq.heappush(pq,[-d,x,y])
                
                heapq.heappop(pq)
        return[[x,y]for d,x,y in pq]