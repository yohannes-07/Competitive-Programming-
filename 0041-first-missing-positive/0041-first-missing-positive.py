class Solution:
    def firstMissingPositive(self, arr: List[int]) -> int:
        n = len(arr)
        i = 0
     
        while i < n:
            correct_position = arr[i] - 1
            
            if i + 1 == arr[i] :
                i += 1
                continue
            
            if 0 <= correct_position < n and  correct_position != i and arr[correct_position] != arr[i]:
                arr[correct_position], arr[i] = arr[i], arr[correct_position]

            else:

                i += 1

    
        for i in range(n):
            if arr[i] - 1 != i:
                return i + 1
         
        return n + 1