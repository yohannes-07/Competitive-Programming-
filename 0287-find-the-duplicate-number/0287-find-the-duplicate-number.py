class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        n = len(arr)
        i = 0
     
        
        while i < n:
            correct_position = arr[i] - 1
            
            if arr[correct_position] == arr[i]:
                i += 1
                continue
            
            if correct_position != i:
                arr[correct_position], arr[i] = arr[i], arr[correct_position]

            else:

                i += 1


        for i in range(n):
            if arr[i] - 1 != i:
                return arr[i]
                
      