class Solution(object):
    def hIndex(self, citations):
        citations = sorted(citations)
        i = 0
        output=0
        while i < len(citations):
            if citations[i] >= len(citations) - i:
                output= len(citations) - i
             
                return output 
            i += 1
        return 0
        

