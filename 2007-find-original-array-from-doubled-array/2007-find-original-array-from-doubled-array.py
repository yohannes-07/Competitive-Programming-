class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        output = []
        c = collections.Counter(changed)
        
        if len(changed) % 2 != 0:
            return []
        
        for i in changed:
            if i== 0 and c[i] >= 2:
                c[i] -= 2
                output.append(i)
                
            elif c[i] != 0 and i > 0 and c[2 * i] != 0:
                c[i] -= 1
                c[2 * i] -= 1
                output.append(i)
            
        if len(output) == len(changed)// 2:
            return output
        else:
            []
        
