class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n, output = len(arr), []
        for i in range(n, 0, -1):
            idx = arr.index(i)
            if idx == i-1:
                continue
            if idx != 0:
                output.append(idx + 1)
                arr[:idx + 1] = arr[:idx + 1][::-1]
            output.append(i)
            arr[:i]= arr[:i][::-1]
            
        return output
        