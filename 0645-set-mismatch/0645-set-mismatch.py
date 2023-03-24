class Solution:
    def findErrorNums(self, arr: List[int]) -> List[int]:
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
                return [arr[i], i + 1]
                
        