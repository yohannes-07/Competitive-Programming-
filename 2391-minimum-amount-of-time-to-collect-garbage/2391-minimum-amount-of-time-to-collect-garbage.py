class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
            prefix = []
            res,  M_idx, G_idx, P_idx = 0, 0, 0, 0
            prefix.append(travel[0])
            
            for i in range(1, len(travel)) :
                prefix.append(prefix[-1] + travel[i])
      
            for i in range(len(garbage)):
                res += len(garbage[i])
                if "M" in garbage[i]:
                    M_idx = i
                if "G" in garbage[i]:
                    G_idx = i
                if "P" in garbage[i]:
                    P_idx = i
           
            res += prefix[M_idx - 1] if M_idx != 0 else 0
            res += prefix[G_idx - 1] if G_idx != 0 else 0
            res += prefix[P_idx - 1] if P_idx != 0 else 0
            
            return res
