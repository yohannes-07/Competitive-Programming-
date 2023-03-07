class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = defaultdict(int)
        self.winner = [0] * len(times)
        
        self.times = times
        leader = -1
        
        i = 0
        for person, time in zip(persons, times):
            self.persons[person] += 1
         
            if self.persons[person] >= self.persons[leader]:
                leader = person
                
            self.winner[i] = leader
            i += 1
     
            

    def q(self, t: int) -> int:
        left, right = 0, len(self.times) -1
        
        while left <= right:
            mid = left + (right - left)// 2
            
            if t < self.times[mid] :
                right = mid -1
                
            else:
                left = mid + 1
         
        return self.winner[left -1]
            
            


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)