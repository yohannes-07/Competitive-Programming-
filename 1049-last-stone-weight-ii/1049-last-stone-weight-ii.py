class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        sums_of_subsets = {0}
        
        for weight in stones:
            sumsOfSubsetsContainCurrWeight = set()
            
            for summ in sums_of_subsets:
                if summ + weight < total/2:
                    sumsOfSubsetsContainCurrWeight.add(summ + weight)   
                    
                elif summ + weight == total/2:
                    return 0
                
            sums_of_subsets |= sumsOfSubsetsContainCurrWeight
            
        return min(total - 2*summ for summ in sums_of_subsets )
         