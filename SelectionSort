class Solution: 
    def select(self, arr, i):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
                
        return minIndex
                
    
    def selectionSort(self, arr,n):
        for i in range(0,n-1):
            minIndex = self.select(arr, i)
            arr[i],arr[minIndex] = arr[minIndex], arr[i]
        return arr
