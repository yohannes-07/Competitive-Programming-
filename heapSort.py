#User function Template for python3

class Solution:
   
    def heappush(self, heap,value):
        heap.append(value)
        current = len(heap) - 1
        self.heapify_up(heap,current)
    
    def heapify_up(self, heap,current):
        parentIdx = (current - 1)//2
    
        while current > 0 and  heap[current] < heap[parentIdx]:
            heap[parentIdx], heap[current] = heap[current], heap[parentIdx]
            current = parentIdx
            parentIdx =  (current - 1)//2
    
    
    def heappop(self, heap):
        if not heap:
            return None
        
        min_value = heap[0]
        heap[0] = heap[-1]
    
        heap.pop()
        current = 0
    
        self.heapify_down(heap,len(heap),current)
        return min_value
    
    def heapify_down(self, arr, n, current):
       
        while current < n:
    
            smallChild = current
            leftChildIdx = 2 * current + 1
            rightChildIdx = 2 * current + 2
    
            if leftChildIdx < n  and rightChildIdx < n:
                smallChild = leftChildIdx if arr[leftChildIdx] <= arr[rightChildIdx] else rightChildIdx
            
            elif leftChildIdx < n and rightChildIdx > 0:
                smallChild = leftChildIdx
            
            elif rightChildIdx < n and leftChildIdx > 0:
                smallChild = rightChildIdx
    
            if arr[current] <= arr[smallChild]: break
                
            arr[current], arr[smallChild] = arr[smallChild],arr[current]
            current = smallChild

    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        heap = []
        
        for num in arr:
            self.heappush(heap, num)
            
        return heap
        
        
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        heapedArr = self.buildHeap(arr.copy(), n)
        
        temp = []
        while heapedArr:
            temp.append(self.heappop(heapedArr))
            
        for i, val in enumerate(temp):
            arr[i] = val
        



# } Driver Code Ends


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends
