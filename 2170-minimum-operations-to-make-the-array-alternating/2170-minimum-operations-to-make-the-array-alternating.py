class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        odd_indices = defaultdict(int)
        even_indices = defaultdict(int)
        
        freqOddIdxElem = (0, 0)
        freqEvenIdxElem = (0, 0)
        
        secondFreqOddIdxElem = (0, 0)
        secondFreqEvenIdxElem = (0, 0)
        
        for i, num in enumerate(nums):
            if i % 2 :
                odd_indices[num] += 1
                    
            else:
                even_indices[num] += 1
        
                    
        for num in odd_indices:
            if odd_indices[num] > freqOddIdxElem[1]:
                freqOddIdxElem , secondFreqOddIdxElem = (num, odd_indices[num]), freqOddIdxElem

            elif odd_indices[num] >= secondFreqOddIdxElem[1]:
                secondFreqOddIdxElem = (num, odd_indices[num])

        for num in even_indices:
            if even_indices[num] > freqEvenIdxElem[1]:
                freqEvenIdxElem , secondFreqEvenIdxElem = (num, even_indices[num]), freqEvenIdxElem

            elif even_indices[num] >= secondFreqEvenIdxElem[1]:
                secondFreqEvenIdxElem = (num, even_indices[num])

                    
        if freqOddIdxElem[0] != freqEvenIdxElem[0]:
            return len(nums) - (freqOddIdxElem[1] + freqEvenIdxElem[1])
        
       
        res = len(nums) - max(freqOddIdxElem[1] + secondFreqEvenIdxElem[1], freqEvenIdxElem[1] + secondFreqOddIdxElem[1])
    
        return res