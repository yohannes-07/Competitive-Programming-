class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        freq = sorted(count.values(), reverse = True)
        most_freq = freq[0]
        no_most_freq = 0
        
        for i in range(len(freq)):
            if freq[i] == most_freq:
                no_most_freq += 1
                
        no_times = (n + 1) * (most_freq -1) + no_most_freq
        return max(len(tasks), no_times)
            