class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dic = {}
        
        for num in arr:
            count = 1
            
            if num - difference in dic:
                count += dic[num - difference]
                
            dic[num] = count

        return max(dic.values())