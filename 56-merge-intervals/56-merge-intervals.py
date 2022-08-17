class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []
        for i in intervals:
            if not output or i[0] > output[-1][1]:
                output.append(i)
            else:
                output[-1][1] = max(output[-1][1], i[1])
        return output
    