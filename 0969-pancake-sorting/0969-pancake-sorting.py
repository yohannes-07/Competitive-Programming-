class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n, pancakeFlips = len(arr), []
        
        #The whole process it selecting the greatest elem and put it at the last position
        # To do so, first put the selected elem at index 0 and then flip arr till its
        # appropriate position
        #Start from the greatest elem and iterate downward...to the next greatest elem
        #note arr[i] is between 1 and len(arr), including & each arr[i] => unique

        for num in range(n, 0, -1):
            numLocationBeforeFlip = arr.index(num)
            
            #if numLocationBeforeFlip is already at last position,
            #continue to the next greatest elem
            if numLocationBeforeFlip == num-1:
                continue

            #if numLocationBeforeFlip is anywhere b/n 0 and num-1,
            #add its position to pancakeFlips arr and reverse the orginal arr till num's initial index
            if numLocationBeforeFlip != 0:
                pancakeFlips.append(numLocationBeforeFlip + 1)
                arr[:numLocationBeforeFlip + 1] = arr[:numLocationBeforeFlip + 1][::-1]

            
            pancakeFlips.append(num)
            arr[:num]= arr[:num][::-1]
            
        return pancakeFlips
        