class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []
        m = len(word1)
        n = len(word2)
        word1 = list(word1)
        word2 = list(word2)
        i, j = 0, 0
        
        while i < m and j < n:
            if word1[i] > word2[j]:
                merge.append(word1[i])
                i += 1
            
            elif word1[i] < word2[j] :
                merge.append(word2[j])
                j += 1
                
            else:
                
                if word1[i:] > word2[j:]:
                    merge.append(word1[i])
                    i += 1

                else:
                    merge.append(word2[j])
                    j += 1

            
                    
        
        merge.extend(word1[i:])
        merge.extend(word2[j:])
        
        return "".join(merge)