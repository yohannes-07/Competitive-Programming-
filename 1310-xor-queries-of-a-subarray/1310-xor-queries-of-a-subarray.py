class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefXor = {-1:1}

        for i in range(len(arr)):
            prefXor[i] = prefXor[i-1] ^ arr[i]
            
       
        res = []
        for i, j in queries:
            
            res.append(prefXor[i-1] ^ prefXor[j])
            
        return res