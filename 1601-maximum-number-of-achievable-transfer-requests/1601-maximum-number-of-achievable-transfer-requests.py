class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        transfers = [0] * n
        
        def backtrack(i, count):
            
            if i >= len(requests):
                
                if all(t == 0 for t in transfers):
                    return count
                
                return 0
                
            transfers[requests[i][0]] -= 1
            transfers[requests[i][1]] += 1
            
            count_included = backtrack(i + 1, count + 1)

            transfers[requests[i][0]] += 1
            transfers[requests[i][1]] -= 1

            count_excluded = backtrack(i + 1, count)

            return max(count_included, count_excluded)
        
        return backtrack(0,0)