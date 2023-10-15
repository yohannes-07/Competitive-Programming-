class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        rank = {}
		
        for p1, p2 in pairs:
            rank[p1] = preferences[p1][:preferences[p1].index(p2)]
            rank[p2] = preferences[p2][:preferences[p2].index(p1)]
       
        count = 0
        
        for p1, prefer in rank.items():
            for p2 in prefer:
                
                if p1 in rank[p2]:
                    count += 1
                    break
                    
        return count