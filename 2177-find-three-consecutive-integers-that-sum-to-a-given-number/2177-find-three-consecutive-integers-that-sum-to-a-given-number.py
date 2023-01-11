class Solution:
    def sumOfThree(self, num: int) -> List[int]:
       
        # 0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33
        if num % 3:
            return []
        
        #find the middle num and subtract and add 1 from the middle num to get
        #the first and last nums which sum to the given num
        res = []
        num2 = num // 3
        
        res.append(num2-1)
        res.append(num2)
        res.append(num2 + 1)
        
        return res