class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x,y):
            
            x = str(x)
            y = str(y)
            if x + y > y + x:
                return -1
            elif x + y == y + x:
                return 0
            elif x + y < y + x:
                return 1
                      
                
        num = sorted(nums, key = cmp_to_key(compare))
        
        if num[0] == 0:
            return "0"
        else:
            return "".join([str(n) for n in num])